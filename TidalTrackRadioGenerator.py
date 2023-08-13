import os
import json
import requests
import tidalapi

CREDENTIALS_FILE = 'credentials.json'


def connect_to_tidal():
    session = tidalapi.Session()
    try:
        if os.path.exists(CREDENTIALS_FILE):
            with open(CREDENTIALS_FILE, 'r') as file:
                credentials = json.load(file)
                session.load_oauth_session(*credentials.values())
        else:
            raise FileNotFoundError
    except (json.JSONDecodeError, FileNotFoundError):
        print("Corrupted or missing credentials file, connecting normally...")
        session.login_oauth_simple()

        credentials = {
            'token_type': session.token_type,
            'access_token': session.access_token,
            'refresh_token': session.refresh_token,
            'expiry_time': session.expiry_time.isoformat() if session.expiry_time else None
        }

        with open(CREDENTIALS_FILE, 'w') as file:
            json.dump(credentials, file)

    print("Successfully connected to Tidal!")
    return session


def create_playlist_based_on_track(session, track_name, reverse_order, limit=None):
    tracks = session.search(track_name, models=[tidalapi.media.Track])
    track_obj = tidalapi.Track(session, tracks['tracks'][0].id)

    try:
        similar_tracks_to_original = track_obj.get_track_radio()
    except requests.exceptions.HTTPError:
        print(f"No Radio found for the track: {track_obj.name}")
        exit()

    track_links = {}
    for i, similar_track in enumerate(similar_tracks_to_original, 1):
        similar_track_obj = tidalapi.Track(session, similar_track.id)
        related_tracks = similar_track_obj.get_track_radio()
        print(str(i) + " " + similar_track_obj.name)
        for related_track in related_tracks:
            track_links[related_track.id] = track_links.get(related_track.id, 0) + 1

    sorted_tracks_by_links = sorted(track_links.items(), key=lambda x: x[1], reverse=reverse_order)
    print(f"Number of similar tracks found: {len(sorted_tracks_by_links)}")

    selected_track_ids = [track_id for track_id, _ in sorted_tracks_by_links[:limit]]
    print(f"Number of selected tracks: {len(selected_track_ids)}")

    playlist = session.user.create_playlist('Around ' + track_name, 'Playlist generated to resemble ' + track_name)
    while True:
        try:
            print(f"Attempting to add {len(selected_track_ids)} tracks...")
            playlist.add(selected_track_ids)
            print(f"{len(selected_track_ids)} tracks added to the playlist")
            break
        except requests.exceptions.HTTPError:
            selected_track_ids = selected_track_ids[:-10]
            if not selected_track_ids:
                print("Failed to create the playlist. All tracks have been removed.")
                break


def main():
    session = connect_to_tidal()
    track_name = input("Track name: ").strip()
    reverse_order = not track_name.startswith('-')
    track_name = track_name[1:] if track_name.startswith('-') else track_name

    try:
        limit = min(int(input("Limit of tracks in the playlist (leave blank for Max 700): ") or 700), 700)
    except ValueError:
        limit = 700

    create_playlist_based_on_track(session, track_name, reverse_order, limit)


if __name__ == "__main__":
    main()
