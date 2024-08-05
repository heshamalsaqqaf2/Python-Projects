import winsound
import time


def play_sound():
    frequency = 2500
    duration = 1000
    for _ in range(5):
        winsound.Beep(frequency, duration)
        time.sleep(0.1)


play_sound()
