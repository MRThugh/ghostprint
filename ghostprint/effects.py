import random
import sys
import time

GLITCH_CHARS = "@#$%&*!?<>/\\|[]{}"


def glitch(text, intensity=3, speed=0.02):
    for char in text:
        for _ in range(intensity):
            fake = random.choice(GLITCH_CHARS)

            sys.stdout.write(fake)
            sys.stdout.flush()

            time.sleep(speed)

            sys.stdout.write("\b")

        sys.stdout.write(char)
        sys.stdout.flush()

        time.sleep(speed)

    print()


def box(text):
    width = len(text) + 2

    print(f"┌{'─' * width}┐")
    print(f"│ {text} │")
    print(f"└{'─' * width}┘")


def banner(text):
    width = len(text) + 8

    print("\n" + "█" * width)
    print(f"██  {text}  ██")
    print("█" * width + "\n")