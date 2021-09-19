"""CP1404/CP5632 Practical - Testing ground for Guitar class."""


from prac_06.guitar import Guitar

CURRENT_YEAR = 2021


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1602
    cost = 820000.0

    guitar = Guitar(name, year, cost)
    other = Guitar("Guitar 2- Electric Boogaloo", 1995, 69420.0)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 5, other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))


if __name__ == '__main__':
    run_tests()
