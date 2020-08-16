"""
	Semaine 6 / Sequence 2
"""

class Point1():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f"Point[{self.x}, {self.y}]"

class Point2(Point1):

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return (11 * self.x + self.y) // 16

class Person:
	def __str__(self):
		return 'test'

def main():
	p1 = Point1(1,1)
	p2 = Point1(1,1)
	for p in [p1,p2]:
		print(p)
	print(len([p1,p2]))
	print(f"==: {p1==p2}")
	print(f"is: {p1 is p2}")

	q1 = Point2(1,1)
	q2 = Point2(1,1)
	print(f"==: {q1 == q2}")
	print(f"is: {q1 is q2}")

	t1,t2 = Point2(10,10), Point2(10,10)
	t3 = Point2(11,11)
	s = {t1,t2,t3}
	print(s)
	t1.x = 100
	print(s)

	p = Person()
	print(p)

if __name__ == "__main__":
	main()

