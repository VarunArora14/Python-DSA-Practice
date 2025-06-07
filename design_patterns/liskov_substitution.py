
# Bad implementation as if we put Bicycle where Vehicle is required (use derived classes where base required then it will fail)
#
# class Vehicle:
#     def start_engine(self):
#       pass
#
# class Car (Vehicle):
#     def start_engine(self):
#         print ("Starting the car engine.")
#
# class Bicycle(Vehicle):
#     def start_engine(self):
#         # This doesn't make sense for a bicycle
#         pass



class Vehicle:
    def start (self):
        raise NotImplementedError("Subclasses must implement this method")

class Car (Vehicle):
    def start (self):
        print ("Starting the car engine")

class Bicycle(Vehicle):
    def start (self):
        print ( "Pedaling the bicycle")
