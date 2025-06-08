from vehicle import Vehicle, VehicleType

class Bike(Vehicle):
    def __init__(self, license_number:str):
        super().__init__(license_number=license_number, vehicle_type=VehicleType.BIKE)
