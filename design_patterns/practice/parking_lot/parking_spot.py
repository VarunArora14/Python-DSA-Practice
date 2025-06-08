from vehicle import Vehicle, VehicleType


class ParkingSpot:
    def __init__(self, spot_number: int, vehicle_type: VehicleType):
        self.spot_number = spot_number
        self.parked_vehicle = None
        self.vehicle_type = vehicle_type

    def occupy_spot(self, parked_vehicle: Vehicle):
        self.parked_vehicle = parked_vehicle

    def get_parked_vehicle(self):
        return self.parked_vehicle

    def get_type(self):
        return self.vehicle_type

    def is_empty(self):
        return self.parked_vehicle is None

    def get_spot_number(self)->int:
        return self.spot_number

    def vacate_spot(self):
        self.parked_vehicle = None
