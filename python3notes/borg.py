
#shared state vs. single instance

class Borg:
  _shared_state={}
  def __init__(self):
     self.__dict__ = self._shared_state

class Singleton(Borg):
  def __init__(self, arg):
     Borg.__init__(self)
     self.val = arg
  
  def __str__(self):
     return self.val


x=Singleton("sin")
print(x)
y=Singleton("another")
print(y)

print(id(x))
print(id(y))

print(vars(x),vars(y))
