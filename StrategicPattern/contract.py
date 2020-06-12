class Contract(object):

	def __init__(self, provider):
		self._provider = provider
		self._number = None

	@property
	def provider(self):
		return self._provider.calculate()

	@property
	def number(self):
		return self._number
	@number.setter
	def number(self,value):
		self._number = value
	
	
	