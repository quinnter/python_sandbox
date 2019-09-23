# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# can be nested inside a tuple

# Create tuple, with or without parenthesis
fruits = ('Apples', 'Oranges', 'Grapes')
fruits3 = "Banana", "Kiwi", "Blueberry"

# empty tuples can be made 
empty_tpl = ()

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])  # Oranges
print(fruits3[1]) # Kiwi

# Can't change value
# fruits[0] = 'Pears'
# would return a TypeError

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

# can also use methods like len
# it's faster to check if an item is part of a set, rather than a list

# Sets can be combined with mathmatical operations
# Union | :  creates new set containing items from both (no duplicates!)
# Intersection & : gets items only in BOTH
# Difference - : gets items from the first set, but not the second
# Symmetric Difference ^ : gets items from either set, but not both

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # {1, 2, 3, 4, 5, 6, 7, 8 ,9}
print(first & second) # {4, 5, 6}
print(first - second) # {1, 2, 3}
print(second - first) # {8, 7, 9}
print(first ^ second) # {1, 2, 3, 7, 8 ,9}


print(fruits_set)
