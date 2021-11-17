python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

python inheritances

  class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)



x = Person("John", "Doe")
x.printname()
