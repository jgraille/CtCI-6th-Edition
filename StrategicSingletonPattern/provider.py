from abc import ABCMeta, abstractmethod
from enum import Enum, unique

class AbsProvider(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def calculate(self):
		""""""

class ProviderOne(AbsProvider):
	PROVIDERONE = "provider1"
	def calculate(self):
		return 10.00

class ProviderTwo(AbsProvider):
	PROVIDERTWO = "provider2"
	def calculate(self):
		return 5.00

class ProviderThree(AbsProvider):
	PROVIDERTHREE = "provider3"
	def calculate(self):
		return 7.00


	
