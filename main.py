"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
"""

import os

JOKE = "The office plant is the only employee who's never called in sick, and HR still won't give it a raise."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
