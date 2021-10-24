import random
from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes a randomness in driving."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but has a chance to not drive at all."""
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
