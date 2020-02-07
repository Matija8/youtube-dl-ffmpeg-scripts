#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import subprocess


def main():
    if len(sys.argv) < 2:
        exit(f"Must have at least 1 argument (URL)!")

    # Avoid ampersands (shell issues), or put URL-s in quotes.
    URLs = sys.argv[1:]

    for URL in URLs:

        # Get formats:
        print(f"Parsing URL: {URL}")
        print("Formats available:\n")
        command = f"youtube-dl -F {URL}".split()
        subprocess.run(command)

        video_format = input("\nEnter video format: ")
        audio_format = input("\nEnter audio format: ")

        command = f"youtube-dl -f {video_format}+{audio_format} {URL} -o %(title)s.%(ext)s".split()
        start = time.time()
        print(f"Getting video from url: {URL}")
        try:
            subprocess.run(command)
        except subprocess.CalledProcessError:
            print("No given format.")
        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")
    print("All done!")
    return
    

if __name__ == "__main__":
    main()
