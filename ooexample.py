class Adder:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def summator(self):
    z = self.x + self.y
    return z

  def setx(self, x):
    self.x = x

  def sety(self, y):
    self.y = y

  def add_hoc_adder(self, x, y):
    return x + y

  def jons_non_add_hoc_adder(self, x, y):
    self.x = x
    self.y = y
    return x + y

if __name__ == '__main__':
  a = Adder(11,22)
  print a.summator()
  print a.jons_non_add_hoc_adder(33,44)
  print a.summator()
  print a.add_hoc_adder(33,44)