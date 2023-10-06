## OOPS
## CLASSES
## OBJEC

# class Car:

#   # attributes/ objects I have defined
#   def __init__(this,engine,doors,tires,color):
#     this.engine = engine
#     this.doors = doors
#     this.tires = tires
#     this.color = color
  
#   def printing(this):
#     print(this.engine)
#     print(this.doors)
#     print(this.tires)
#     print(this.color)

# Thar = Car("V6",3,"Michellin","Black")
# Thar.printing()


# NOW EVERYONE MAKE A CLASS BIKE
# IN WHICH MAKE ATTRIBUTES OF COLOR, BRAND, TIRES

# class Bike:
#   def __init__(self,color,brand,tires):
#     self.color = color
#     self.brand = brand
#     self.tires = tires

#   # I WANT TO USE THE PROPERTIES so that I can implement them inside a function
#   def printing(self):
#     print(self.color)
#     print(self.brand)
#     print(self.tires)
 

# Bullet = Bike("Black","Royal Enfield","MRF")
# Bullet.printing()

# INEHRITANCE

# THERE ARE TWO CLASSES --> PARENT CLASS
# CHILD CLASS
class Vehicles:

  # attributes/ objects I have defined
  def __init__(this,engine,tires,color):
    this.engine = engine
    this.tires = tires
    this.color = color
  
  def printing(this):
    print(this.engine)
    print(this.tires)
    print(this.color)

class Car(Vehicles):
  def __init__(this, engine, doors, tires, color):
   super().__init__(engine, tires, color)
   this.doors = doors

  def printing(this):
    print(this.engine)
    print(this.tires)
    print(this.color)
    print(this.doors)


BALENO = Car("v4",5,"Apollo","Blue")
BALENO.printing()
