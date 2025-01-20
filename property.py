# https://www.programiz.com/python-programming/property
class Celsius:
    def __init__(self, temperature=0, name="varun"):
        self.temperature = temperature
        self.name = name
    
    def fahrenheit(self):
        return self.temperature*1.8 +32
    
    @property
    def temperature(self):
        print("Getting value....")
        return dir(self)
    
    @temperature.setter
    def temperature(self, value):
        print("Setting value")
        if value < -273.15:
            raise ValueError("Temperature less than 273.15 not acceptable")
        self._temperature=value
    
    # temperature = property(get_temperature, set_temperature)
        
c = Celsius(1)    
print(c.temperature)
# print(c.fahrenheit())

# property allows you to create a property and then use getters and setters. You do not have to change old code for setting/getting values
# more here - https://www.freecodecamp.org/news/python-property-decorator/

# python class variables are declared via _varname