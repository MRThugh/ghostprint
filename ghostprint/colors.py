RESET = "\033[0m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"


def color(text, color_code):
    return f"{color_code}{text}{RESET}"


def gradient(text):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

    output = ""

    for index, char in enumerate(text):
        output += colors[index % len(colors)] + char

    output += RESET

    return output