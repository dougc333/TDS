#what is the difference between __str__ and __repr__

class First:
  def __init__(self):
    self.name="First"
  
  def __str__(self):
    return f'name:{self.name}'

 
class Second:
  def __init__(self):
    self.name='Second'

  def __str__(self):
    return 'name:'+self.name
 
  def __repr__(self):
    return '__repr__ for Second'    

class Third:
 def __init__(self):
   self.name='Third'

 #call object repr and str, we dont need object arg in class defn for python3

first = First()
print('first:',first)

second = Second()
print('second:',second)

third = Third()
print('third:',third)

#print calls the __str__ method
print(first.__repr__)
print(second.__repr__)
print(third.__repr__)

