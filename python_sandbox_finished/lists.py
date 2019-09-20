# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5, 6 , 7 , 8]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

# list slices, can also work on tuples
print(fruits[1:3]) # Oranges, Mangos, includes first not last
print(fruits[:3])  # Apples, Oranges, Mangos, from start until number
print(fruits[2:])  # Mangos, Blueberries, from number until end
print(numbers[::2]) # 1, 3, 5, 7 ; every other?
print(numbers[1:8:2]) # 2, 4, 6 ,8 ; starting with index 1, until index 8, skip 2 index
print(numbers[2:9:3]) # 3, 6 ; starting with index 2, until index 9, skip 3 index
print(numbers[9:2:-3]) # 8, 5 ; starting with index 2, until index 9, skip 3 index
# if last number is negative, happens backwards
print(numbers[1:-1]) # 2, 3 ,4 ,5 ,6 ,7


# list comprehension ; a list that obey a rule
cubes = [i**3 for i in range(5)]
print(cubes)
# comprehension can also includes if statements
# but if the range is too extensive you can come across MemoryErrors
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

# LIST FUNCTIONS

nums = [55, 44, 33, 22, 11]

# All : returns true if all are true
if all([i > 5 for i in nums]):
   print("All larger than 5")

# Any : returns true if at least one is true
if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

# Enumerate : itereates through values and indices 
# (0, 55) /n(1, 44) n/(2, 33) etc
for value in enumerate(nums):
   print(value)

