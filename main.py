"""
TikTok Video Downloader
"""

import os
from typing import Optional
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_proxy_url(video_id: str) -> str:
    """Return the proxy URL for the given video ID."""
    return f"https://proxitok.pussthecat.org/@olga.gabrys/video/{video_id}"


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


def main() -> None:
    """Main function to run the TikTok video downloader."""
    input_file = "tiktok_links.txt"
    output_folder = "TikToks"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, "r", encoding="utf-8") as file:
        tiktok_links = file.readlines()

    for i, link in enumerate(tiktok_links, 1):
        link = link.strip()
        video_id = link.split("/")[-2]

        proxy_url = get_proxy_url(video_id)
        download_url = get_download_url(proxy_url)

        if download_url:
            output_filename = os.path.join(
                output_folder, f"{str(i).zfill(3)}_{video_id}.mp4"
            )
            download_video(download_url, output_filename)
        else:
            print(f"Download button not found for {video_id}")


if __name__ == "__main__":
    main()
