# Itertools is a standard library, with useful iterative functions
# more functions here https://docs.python.org/3/library/itertools.html

from itertools import count # counts up infinitely from a value
from itertools import cycle # infinitely iterates though a iterable
from itertools import repeat # repeats an object, infinitely or a specific number
from itertools import takewhile # takes item from an iterable, when a predicate function remains true
from itertools import accumulate # returns running total of values in an iterable
from itertools import chain # combines several iterables into one long one
from itertools import product 
from itertools import permutations # products/permutations : accomplish a task with all possible combinations

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

for i in count(3):
    print(i)
    if i >= 11:
        break

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 

