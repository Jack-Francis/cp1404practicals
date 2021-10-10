

from prac_08.unreliable_car import UnreliableCar

half_car = UnreliableCar("50% Car", 200, 50)
# 50 reliability indicates this car should drive only 50% of the time
for i in range(10):
    # run 10 tests
    half_car.drive(10)
    print(half_car)
