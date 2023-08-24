# 

class Vehicle: # SUper class / Parent class
  def __init__(this,Engine,Brakes,Tires):
    this.Engine= Engine
    this.Brakes= Brakes
    this.Tires= Tires
  def Printing(this):
    print(this.Engine)
    print(this.Brakes)
    print(this.Tires)

class Cars(Vehicle): # it's child class
  def __init__(this, Engine, Brakes, Tires,Color,Brand):
    this.Color= Color
    this.Brand= Brand
    Vehicle.__init__(this,Engine,Brakes,Tires)
  def Printing(this):
     print(this.Engine)
     print(this.Brakes)
     print(this.Tires)
     print(this.Color)
     print(this.Brand)

# PARENT CLASS CALLING
corrola= Vehicle("V6","Ceramic","Apollo")
corrola.Printing() # this is I am calling to vehicle 

print()

# CHILD CLASS CALLING
Mustang = Cars("V8","Mambo Brakes","Michellin","Black","Ford")
Mustang.Printing()


# You have inherited your Dad's property
# but your Dad will not inherit your property
