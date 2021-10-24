"""
CP1404/CP5632 Practical - Suggested Solution
Sort files 1 program
"""
import os


def main():
    """Move files into folders based on their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print(f"{extension}/{filename}")
        os.rename(filename, f"{extension}/{filename}")


main()
