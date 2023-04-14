"""This module handles argument parsing for the TikTok Video Downloader."""

import argparse
from typing import Tuple


def parse_arguments() -> Tuple[str, str, str]:
    """
    Parse command-line arguments for the TikTok Video Downloader.

    Returns:
        Tuple containing input_file, output_folder, and proxy_url.
    """
    parser = argparse.ArgumentParser(description="TikTok Video Downloader")
    parser.add_argument(
        "-i",
        "--input-file",
        default="tiktok_links.txt",
        help="Path to the input file containing TikTok video links",
    )
    parser.add_argument(
        "-o",
        "--output-folder",
        default="TikToks",
        help="Path to the folder where downloaded videos will be saved",
    )
    parser.add_argument(
        "-p",
        "--proxy-url",
        default="https://proxitok.pussthecat.org",
        help="The proxy URL to be used for downloading videos",
    )
    args = parser.parse_args()

    return args.input_file, args.output_folder, args.proxy_url
