import sys
import time


def typewrite(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    print()


def loading(text="Loading", duration=3):
    chars = ["⠁", "⠂", "⠄", "⠂"]

    end_time = time.time() + duration
    index = 0

    while time.time() < end_time:
        char = chars[index % len(chars)]

        sys.stdout.write(f"\r{text} {char}")
        sys.stdout.flush()

        time.sleep(0.1)

        index += 1

    sys.stdout.write(f"\r{text} ✓\n")