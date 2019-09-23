# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1


# Extend class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())

class Dog1:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog1("Fido", "brown")
print(fido.legs)
print(Dog1.legs)

# classes can also have class attributes, by assigning variables inside the class (legs)
# AttributeError when you try to access an attribute that does not exist

# Inheritance 
class Animal: # SUPERCLASS
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def noise(self):
    print('Hello!')

class Cat(Animal): # SUBCLASS
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def noise(self):
    print("Woof!")

# Cat and Dog are both classes that share a name and colour attribute
# if a subclass inherits from another with the same attributes or methods, it overrides them.

fido = Dog("Fido", "brown")
salem = Cat("Salem", "black")
fido.noise()
salem.noise()


# Inheritance can also be indirect

class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B):
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

# SUPER
# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.

class A1:
  def spam(self):
    print(1)

class B1(A1):
  def spam(self):
    print(2)
    super().spam()
            
B1().spam()