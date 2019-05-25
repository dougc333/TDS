def a(x):
  return repr(x)

def a1(x):
  return x.__repr__()

#def a2(x):
#  return `x` python3 no longer recognizes the bactick


import dis
print (dis.dis(a))
print(dis.dis(a1))

