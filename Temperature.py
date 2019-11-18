"""
	Semaine 6 / Sequence 1
"""

# Une version de création d'un objet Température Version Niveau 0
class Temperature1:
	def __init__(self, degre):
		self.degre = degre

	def get_temperature(self):
		return (self.degre)
# Une version de création d'un objet Température Version niveau 1 
class Temperature2:
	def __init__(self, degre):
		self.degre = degre

	def __repr__(self):
		return f"La température est de {self.degre} °C"
#Une version possible mais pas la plus répandue
#réf : https://www.programiz.com/python-programming/property
class Temperature3:
	def __init__(self,temperature = 0):
		self.temperature = temperature

	def to_fahrenheit(self):
		return ((self.temperature * 1.8) + 32)

	def get_temperature(self):
		print("Getting value")
		return self._temperature

	def set_temperature(self, value):
		if (value < -273):
			raise ValueError("Value not alowed")
		print("Setting value")
		self._temperature = value

	temperature = property(get_temperature,set_temperature)
#Version la plus courante
class Temperature4:
	def __init__(self,temperature = 0):
		self._temperature = temperature
	
	def to_fahrenheit(self):
		return ((self.temperature * 1.8) + 32)
	@property
	def temperature(self):
		return self._temperature
		
	@temperature.setter
	def temperature(self, value):
		if (value < -273):
			raise ValueError("Value not allowed")
		self._temperature = value


def main():
	"""
	temperature1 = Temperature1(-10)
	print(temperature1.degre)
	print(temperature1.get_temperature())
	print(f"La température est de {temperature1.get_temperature()} °C")
	temperature2 = Temperature2(11)
	print(temperature2)
	print(temperature2.degre)
	"""
	
	c = Temperature4()
	c.temperature = 40
	print(c.to_fahrenheit())



if __name__ == "__main__":
	main()