from vehicle import Vehicle, VehicleType

class Car(Vehicle):
    def __init__(self, license_number:str):
        super().__init__(license_number=license_number, vehicle_type=VehicleType.CAR)
