from prac_08.silver_service_taxi import SilverServiceTaxi

taxing_taxi = SilverServiceTaxi("Taxing Taxi", 100, 2)
taxing_taxi.drive(18)
print(taxing_taxi)
print(f"${taxing_taxi.get_fare()}")
