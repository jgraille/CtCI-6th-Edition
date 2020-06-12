from contract import Contract
from provider import ProviderOne,ProviderTwo,ProviderThree

def main():
	contract = Contract(ProviderOne())
	cost_providerone = contract.provider
	cost_providertwo = Contract(ProviderTwo()).provider
	cost_providerthree = Contract(ProviderThree()).provider
	contract.number = 13456
	assert cost_providerone == 10.00
	assert cost_providertwo == 5.00
	assert cost_providerthree == 7.0
	
if __name__ == "__main__":
	main()