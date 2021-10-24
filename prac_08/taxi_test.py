"""CP1404/CP5632 Practical - Client code to use the Taxi class."""

from prac_08.taxi import Taxi

# 1
prius_1 = Taxi("Prius 1", 100)
# 2
prius_1.start_fare()
prius_1.drive(40)
# 3
prius_1.get_fare()
print(prius_1)
# 4
prius_1.start_fare()
prius_1.drive(100)
# 5
prius_1.get_fare()
print(prius_1)
