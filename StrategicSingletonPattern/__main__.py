from contract import Contract
from provider import ProviderOne,ProviderTwo,ProviderThree
from benchmark import BenchMark

def main():
	contract = Contract(ProviderOne())
	cost_providerone = Contract(ProviderOne()).provider
	cost_providertwo = Contract(ProviderTwo()).provider
	cost_providerthree = Contract(ProviderThree()).provider
	contract.number = 13456
	assert cost_providerone == 10.00
	assert cost_providertwo == 5.00
	assert cost_providerthree == 7.0
	bench1 = BenchMark('bench1')
	bench2 = BenchMark('bench2')
	print(bench1)
	print(bench2)

	print("test")
if __name__ == "__main__":
	main()