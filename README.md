# Tidal Track Radio Generator

Version 1.0 - No Changelog

## Overview

The Tidal Track Radio Generator is a Python script that creates a Tidal playlist by generating a **"two-degree" radio around a selected track**. It searches for tracks similar to the chosen one, then finds tracks similar to those, creating a playlist that's two degrees removed from the original. By extending the concept of a traditional radio, this tool provides a richer and more diverse musical experience.

## Acknowledgments

Special thanks to the [Tidal API](https://tidalapi.netlify.app/) developers and the open-source community for making this project possible. Your contributions to the world of music and programming are greatly appreciated.

## License

This project is licensed under the MIT License - see the [License](LICENSE) file for details.

## Installation

### Prerequisites

    Python 3.7 or higher
    Tidal account

### Dependencies

The following Python packages are required:

    tidalapi
    requests

You can install them using the following command:

    $ pip install tidalapi requests

### Installation

    Clone the repository or download the script.

### Running the Script

    $ python TidalTrackRadioGenerator.py

At the first launch, the script saves your Tidal Tokens of connections to the credentials file for a week until they expire.

Follow the prompts to enter the track name and other preferences.
You can reverse the order of the sorted playlist by adding minus symbol before the track's name.
For example:

    -Hey Jude

You can try to add 700 tracks to the playlist, but sometimes it doesn't work because of the API limitation. In this case, the script tries to add as many tracks as possible.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or open a pull request.

## Support

For any questions or support, please [email me](mailto:tidalsimilarity.anybody604@silomails.com?subject=Need%20Support%20with%20your%20incredible%20tool) or create an issue in the repository.

## Author

Initial work by [Siloli](https://github.com/siloli)
