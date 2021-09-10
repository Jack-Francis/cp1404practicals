"""
CP1404/CP5632 Practical
Email to name dictionary
"""

# Solutions were viewed after completion to fix/optimise code


def main():
    """Program for a dictionary of emails-to-names."""
    email_to_name = {}      # Dictionary
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_check = input(f"Is your name {name}? (Y/n) ")
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
