#inner class singleton
class Singleton:
  class __inner:
     def __init__(self):
        print("inner init")
        self.val = None
     def __str__(self):
        print("inner str")
        return self.val
  instance = None
  def __new__(cls):
     print("__new__")
     if not Singleton.instance:
         Singleton.instance = Singleton.__inner()
     return Singleton.instance
  def __getattr__(self, name):
     print("getattr")
     return getattr(self.instance, name)
  def __setattr__(self , name):
     print("setattr")
     return setattr(self.instance,name)

x = Singleton()
x.val="a"
print(x.__repr__())
