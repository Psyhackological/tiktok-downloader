"""
TikTok Video Downloader Library
"""

from typing import Optional
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_proxy_url(video_id: str, proxy_base_url: str) -> str:
    """Return the proxy URL for the given video ID and proxy base URL."""
    return f"{proxy_base_url}/@olga.gabrys/video/{video_id}"


def get_download_url(proxy_url: str) -> Optional[str]:
    """Return the download URL for the given proxy URL."""
    response = requests.get(proxy_url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    download_button = soup.find("a", class_="button is-success", string="No watermark")

    if download_button and isinstance(download_button, Tag):
        return f'https://proxitok.pussthecat.org{download_button["href"]}'
    return None


def download_video(download_url: str, output_filename: str) -> None:
    """Download the video and save it to the output filename."""
    video_response = requests.get(download_url, timeout=10)

    with open(output_filename, "wb") as video_file:
        video_file.write(video_response.content)

    print(f"{output_filename} was downloaded successfully.")
