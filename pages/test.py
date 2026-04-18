x = "global"

def outer():
  global x
  x = "enclosing"
  def inner():
    nonlocal x
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)
