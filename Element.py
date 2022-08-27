class Element:

  def __init__(self, name, symbol, mass):
    self.name = name
    self.symbol = symbol
    self.mass = mass

  def getName(self):
    return self.name
    
  def getSymbol(self):
    return self.symbol
    
  def getMass(self):
    return self.mass
    
# carbon = Element("Carbon", "C", "12.01")
# carbon.getMass()