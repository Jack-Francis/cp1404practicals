from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.5
    # Flagfall cost of $4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with the flagfall value."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the silver service taxi trip."""
        return self.flagfall + super().get_fare()
