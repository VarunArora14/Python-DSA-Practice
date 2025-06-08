from level import Level
from parking_lot import ParkingLot
from car import Car
from truck import Truck
from bike import Bike


class ParkingLotDemo:
    def run(self):
        parking_lot = ParkingLot()
        parking_lot.add_level(level=Level(1, 100))
        parking_lot.add_level(level=Level(2, 50))

        car1 = Car("car1")
        car2 = Car("car2")

        bike1 = Bike("bike1")

        truck1 = Truck("truck1")

        slot_number, could_park = parking_lot.park_vehicle(car1)
        parking_lot.park_vehicle(car2)
        parking_lot.park_vehicle(bike1)
        parking_lot.park_vehicle(truck1)

        parking_lot.unpark_vehicle(car2)

        parking_lot.display_availability()

if __name__ == "__main__":
    p = ParkingLotDemo()
    p.run()