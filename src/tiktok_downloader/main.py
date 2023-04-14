"""
TikTok Video Downloader
"""

import os
from tiktok_downloader.lib.downloader import (
    get_proxy_url,
    get_download_url,
    download_video,
)
from tiktok_downloader.lib.argument_parsing import parse_arguments


def main() -> None:
    """Main function to run the TikTok video downloader."""
    input_file, output_folder, proxy_base_url = parse_arguments()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_file, "r", encoding="utf-8") as file:
        tiktok_links = file.readlines()

    # Calculate the width for zfill
    zfill_width = len(str(len(tiktok_links)))

    for i, link in enumerate(tiktok_links, 1):
        link = link.strip()
        video_id = link.split("/")[-2]

        proxy_url = get_proxy_url(video_id, proxy_base_url)
        download_url = get_download_url(proxy_url)

        if download_url:
            output_filename = os.path.join(
                output_folder, f"{str(i).zfill(zfill_width)}_{video_id}.mp4"
            )
            download_video(download_url, output_filename)
        else:
            print(f"Download button not found for {video_id}")


if __name__ == "__main__":
    main()
