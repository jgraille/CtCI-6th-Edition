class Provider:

	def __init__(self):
		self._providerone = "provider1"
		self._providertwo = "provider2"
		self._priderthree = "provider3"

	@property
	def providerone(self):
		return self._providerone
	
	@property
	def providertwo(self):
		return self._providertwo
	
	@property
	def providerthree(self):
		return self._providerthree
	