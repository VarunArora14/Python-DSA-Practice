from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.levels: list[Level] = []

    def add_level(self, level: Level)->None:
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> (int, bool):
        for level in self.levels:
            slot_number = level.park_vehicle(vehicle=vehicle)
            if slot_number != -1:
                print(
                    f"Car parked in level: {level.level_number} with slot number: {slot_number}"
                )
                return slot_number, True
        print(f"Unable to park vehicle of number: {vehicle.get_licence_number()}")
        return -1, False

    def unpark_vehicle(self, vehicle: Vehicle)->bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle=vehicle):
                print(f"Vehicle of number: {vehicle.get_licence_number()} unparked!")
                return True
        return False

    def display_availability(self):
        for level in self.levels:
            level.display_available_spots()

