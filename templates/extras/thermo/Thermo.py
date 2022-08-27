class Thermo:

	def __init__(self, compound, entropy, enthalpy, gibbs):
		self.compound = compound
		self.enthalpy = enthalpy
		self.entropy = entropy
		self.gibbs = gibbs

	def getCompound(self):
		return self.compound

	def getEnth(self):
		return self.enthalpy

	def getEntr(self):
		return self.entropy

	def getGibbs(self):
		return self.gibbs

