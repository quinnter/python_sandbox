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

print(fruits_set)
