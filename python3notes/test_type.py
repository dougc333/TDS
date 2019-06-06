#type() uses type.__call__() and call() uses type.__new__ and type.__init__
#python2 classes inherit from type
#python3 clasess inherit from object


class A: 
  print("class A")
  def __call__(self):
     print("A call")
  def __init__(self):
     print("A init")

class B: 
  print("class B")
  def __init__(self):
    print("B init")
  def __new__(self):
    print("B new")

print("x=A()")
x=A()
print("print x")
print(x)
print("type(x)")
print(type(x))
print("x1=A()")
x1=A()
print("print x1")
print(x1)
print("exec y=B()")
y=B()
print("print y")
print(y)
print("type y")
print(type(y))
print("y1=B()")
y1=B()

print("--------")
print(x.__repr__())
print(x1.__repr__())
print(y.__repr__())
print(y1.__repr__())



