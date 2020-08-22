"""
Input: alarm time, sound file, message
Output: set off alarm
"""

import winsound
import time
import datetime

def set_alarm(time_in_seconds, sound_file_path, message):
    time.sleep(time_in_seconds)
    winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)
    print(message)


if __name__ == "__main__":
    set_alarm(5, "rooster2.wav", "Good Morning... Wake up..")