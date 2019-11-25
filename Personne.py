class Personne:

	def __init__(self,nom,age,mail):
		self.nom = nom
		self.age = age
		self.mail = mail

	def __repr__(self):
		return f"{self.nom}, {self.age} ans, {self.mail}"

	def sendmail(self, subject, body):
		print(f"To: {self.mail}")
		print(f"Subject: {subject}")
		print(f"Body: {body}")

def main():
	personne1 = Personne('Pierre', 23,'pierre@gmail.com')
	personne2 = Personne('Jean-Pierre', 22,'jpierre@gmail.com')
	personne3 = Personne('Jean-Paul', 24,'jpaul@gmail.com')
	personnes = [personne1,personne2,personne3]


	index_par_nom = {personne.nom: personne for personne in personnes}
	personne1.age += 1
	print(personne1.sendmail('Les popcorns','Je veux manger des popcorns'))

if __name__ == '__main__':
	main()