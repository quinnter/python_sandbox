# map examples

def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]

# map with a function
result = list(map(add_five, nums))
print(result)

# map with a lambda function 
result2 = list(map(lambda x: x+5, nums))
print(result2)

# fiter examples

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)