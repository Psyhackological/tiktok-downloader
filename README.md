<p align="center">
  <img src="img/tiktok_downloader_logo.svg" alt="TikTok Downloader">
</p>

<h1 align="center">
  TikTok Downloader
</h1>

![asciinemagifgenerator](img/tiktok_downloader.gif)

<p align="center">
  This script downloads TikTok videos using a provided list of URLs and saves them into a specified folder with a custom naming format.
</p>

# Table of contents
1. [Main features](#main-features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Troubleshooting](#troubleshooting)
5. [Usage with examples](#usage-with-examples)
6. [Contributing](#contributing)
7. [License](#license)

## Main features
- Download TikTok videos without a watermark.
- Save videos with custom naming format (e.g., 001_, 002_, ...).
- Automatically create the output folder if it doesn't exist.
- Provide a list of TikTok URLs in a text file to download multiple videos at once.

## Requirements
- Python 3.6 or higher
- requests
- beautifulsoup4

## Installation
1. Clone the repository:

```bash
git clone https://github.com/Psyhackological/tiktok_downloader.git`
```

2. Navigate to the project directory and install the required packages:

```bash
cd tiktok_downloader
pip install -r requirements.txt
```


## Troubleshooting
If you face any issues while using the script, please open an issue on the GitHub repository, and provide as much information as possible, including the error message and the list of TikTok URLs you're trying to download.

## Usage with examples
1. Create a text file containing a list of TikTok URLs, one per line.
2. Run the script:

```bash
python scrapper.py
```

3. The downloaded videos will be saved in the "TikToks" folder with the custom naming format.

## Contributing
If you'd like to contribute to the project, please submit a pull request or open an issue with your suggestions or bug reports.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
