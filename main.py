"""The Book That Fought Back: a rooftop spellbook answers an octopus with swords.

Copy the original JPEG artwork unchanged to the competition's entry.png path.
"""

import os
import shutil


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "octopus.jpg")
    if not os.path.isfile(source):
        raise SystemExit(f"Entry image is missing: {source}")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, "entry.png"))


if __name__ == "__main__":
    main()
