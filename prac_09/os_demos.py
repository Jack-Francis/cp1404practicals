"""
CP1404/CP5632 Practical
Cleanup Files program
"""
import os


def main():
    """Cleanup inconsistent song lyrics file names."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name_string = ""
    for character in new_name:
        if character.isupper():
            character = f"_{character}"
        new_name_string = f"{new_name_string}{character}"
    newer_name_string = ""
    for i in range(0, len(new_name_string)):
        if i != 0:
            newer_name_string = newer_name_string + new_name_string[i]
    new_name = filename.replace("__", "_").replace("(_", "(")
    return new_name


main()
