from enum import Enum


class VehicleType(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


class Vehicle:
    def __init__(self, license_number: str, vehicle_type: VehicleType):
        self.licence_number = license_number
        self.vehicle_type = vehicle_type

    def get_type(self):
        return self.vehicle_type

    def get_licence_number(self):
        return self.licence_number

