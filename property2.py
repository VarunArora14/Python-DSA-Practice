class House:

	def __init__(self, price, username):
		print("Getter called")
		self._price = price
		self._username = username

	@property
	def price(self):
		print(f"getter called => username: {self._username}")
		return self._price
	
	@price.setter
	def price(self, new_price):
		print("setter called")
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price

h = House(100,"varun")
print(h.price) # you can access _price but should not by convention
h.price=120.1
print(h.price)
'''
https://www.programiz.com/python-programming/property

# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
'''