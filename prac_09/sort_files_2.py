"""
CP1404/CP5632 Practical
Sort files 2 program
"""
import os


def main():
    """Move files into user named folders based on their extension."""
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, f"{extension_to_category[extension]}/{filename}")


main()
