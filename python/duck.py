#in a static type language this doesnt work


class Animal:
  pass

class Duck:
  def fly(self):
    print('duck flying')

class Airplane:
  def fly(self):
    print('airplane flying')

class Whale:
  def fish(self):
    print("whale fishing")


for animal in Duck(), Airplane(), Whale():
   animal.fly()

