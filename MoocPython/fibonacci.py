"""
	Semaine 1 / Sequence 4
"""
from argparse import ArgumentParser
import sys

def fibonnacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonnacci(n-1) + fibonnacci(n - 2)
"""
Autre Solution avec la librairie argparse
def main():
	parser = ArgumentParser()
	parser.add_argument(dest="entier", type = int, help = "entier d'entrée")
	input_args = parser.parse_args()
	entier = input_args.entier
	print(f"res = {fibonnacci(entier)}")
"""
def main():
	if (sys.argv[1]):
		try:
			print(f"res = {fibonnacci(int(sys.argv[1]))}")
		except ValueError:
			print("Rentrer une valeur numerique")	


if __name__ == "__main__":
	main()

