# lesson: class ivar are under class declaration, instacnce ivars are under init
#class ivars are valid across all instances. instance ivars can vary between instances
#instances are separate copies in memory of classes
#lesson: creating classes/instances using cls(args) instead of instance=Class()
#
# usage differences staticmethod and classmethod decorator
#

class A:
  class_ivar = None
  def __init__(self,args):
     print("init")
     self.instance_ivar = args
  @classmethod
  def foo1(cls,foo1_arg):
     print("foo1")
     instance_ivar = foo1_arg
     print("foo1 args:",foo1_arg, " instance_ivar:",instance_ivar) 
     return A("a") #this calls __init__
     
  def foo2(cls,foo2_arg):
     print("foo2")
     return cls(foo2_arg) #should see foo2_arg = val
 
x = A("A class")
print(x)

print("class method")
A.foo1("a")
b = A.foo1("b")
#doesnt call __init__()
print("b:",b)
print("create c is there __init__?")
c = A("c")
print("c:",c)

