# Generators : iterable like lists/tuples
# doesn't allow indexing but can be iterated through for loops

# use in functions with yield statements
# yield returns a sequence of values, where return is one specified value
# when you want to iterate over a sequence but don't want to store the values in memory
# which means they could be infinite

def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

# def infinite_sevens():
#   while True:
#     yield 7
        
# for i in infinite_sevens():
#   print(i)

def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

# DECORATORS : wrap a function, modifying it's behaviour
# closures
# func that takes a func as an arg, return another func?

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)
# this is the longer way of doing VVV 
# @ is sometimes called pie syntax

@my_decorator
def say_whee():
    print("Whee!")


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

 # decorator_function returns wrapper function which is waiting to be executed

# def display():
#     print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display == wrapper_function waiting to be executed
# when it's executed it executes the original_function which is display

# decorated_display()

# why?
# easily add functionality to existing functions, by adding functionality to the wrapper
# in this example the wrapper is display?

@decorator_function
def display():
    print('display function ran')

display()

# ^^^ How decorators should be written

