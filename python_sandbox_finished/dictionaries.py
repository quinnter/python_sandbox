# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# similar to an object literal

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# trying to access a key they doesn't exist ex: 'gender' returns KeyError

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# you can also you in/not in to check keys
print('first_name' in person) #true
print('gender' in person)     #false
print('gender' not in person) #true

# get method, similar to index but returns None if not found
print(person.get('first_name')) # John
print(person.get('email'))      # None
print(person.get(12345, "not in dictionary")) # not in dictionary
print(person.get('last_name', "not in dictionary")) # Doe



# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
