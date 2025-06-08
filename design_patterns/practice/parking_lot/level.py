from typing import List

from parking_spot import ParkingSpot
from vehicle import Vehicle, VehicleType


class Level:
    def __init__(self, level_number: int, nums_spots: int):
        self.level_number = level_number
        self.parking_spots: List[ParkingSpot] = []
        self.parking_spots.extend([ParkingSpot(i, VehicleType.BIKE) for i in range(min(nums_spots, 20))])
        self.parking_spots.extend([ParkingSpot(i, VehicleType.CAR) for i in range(20, min(nums_spots, 80))])
        self.parking_spots.extend([ParkingSpot(i, VehicleType.TRUCK) for i in range(80, min(nums_spots, 120))])


    def add_parking_spot(self, parking_spot: ParkingSpot):
        self.parking_spots.append(parking_spot)

    def park_vehicle(self, vehicle: Vehicle):
        slot_number = -1
        for idx in range(len(self.parking_spots)):
            spot = self.parking_spots[idx]
            if spot.is_empty() and spot.get_type().value >= vehicle.get_type().value:
                spot.occupy_spot(parked_vehicle=vehicle)
                slot_number = spot.get_spot_number()
                break

        return slot_number

    def unpark_vehicle(self, vehicle: Vehicle):
        for idx in range(len(self.parking_spots)):
            spot = self.parking_spots[idx]
            if spot.get_parked_vehicle() == vehicle:
                spot.vacate_spot()
                return True

        return False

    def display_available_spots(self):
        for spot in self.parking_spots:
            if spot.is_empty():
                print(
                    f"Parking Spot: {spot.get_spot_number()} Available"
                )
            else:
                print(
                    f"Parking Spot: {spot.get_spot_number()} Occupied"
                )
