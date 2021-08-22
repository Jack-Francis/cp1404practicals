"""
CP1404/CP5632 - Practical
Temperature Conversion Program
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def c_to_f(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
