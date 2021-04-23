from shutil import which
import sys
import yaml
import os
import time


if __name__ == '__main__':

    if not which("youtube-dl"):
        print("You need to install youtube-dl first")
        sys.exit(1)

    with open(r'config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        username = config["username"]
        password = config["password"]
        baseDir = config["dir"]
        sleepInterval = config["sleep"]
        courses = config["courses"]

    for course in courses:
        print(f"Starting download of {course}")
        cmd = (f"youtube-dl --username '{username}' --password '{password}'"
               f" -o '{baseDir}/%(playlist)s/%(chapter_number)s"
               f" - %(chapter)s/%(playlist_index)s - %(title)s.%(ext)s'"
               f" --sleep-interval {sleepInterval}"
               f" https://app.pluralsight.com/library/courses/{course}/"
               f"--playlist-start 1")
        os.system(cmd)
        time.sleep(sleepInterval)
