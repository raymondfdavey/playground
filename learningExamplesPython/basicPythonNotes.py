
### FROM KAGGLE
### MATHEMATICAL ORDER OF OPERATIONS

# symbol // rounds down to nearest integer
print(9 / 4) # prints 2.25
print(9 // 4) # prints 2

#order of operation is multiply and divide first

print(10 + 10 * 2) # 30
print((10 + 10) * 2) # 40

print(10 + 10 ** 2) # 110
print((10 + 10) ** 2) # 400
print(10 * 10 ** 2) # 400

print(min(1, 2, 3)) # 1
print(max(1, 2, 3)) # 3

print(abs(32)) # 32
print(abs(-32)) # 32

print( 10 * 10 ** 2 ) # 1000
print((10 * 10) ** 2) # 10000

### HELP AND DOCSTRINGS

# help(round)
print(round(1.2324, 2))
# Python isn't smart enough to read my code and turn it into a nice English description. However, when I write a function, I can provide a description in what's called the docstring.

# Docstrings
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call help() on a function, it shows the docstring.

# Adding optional arguments with default values to the functions we define turns out to be pretty easy:

def greet(who="Colin"):
    print("Hello,", who)
    
greet() # Hello, Colin
greet(who="Kaggle") # Hello, Kaggle
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world") # Hello, world

num = 1232421.134679
print(round(num, -5)) # 1200000.0 -> round with negative second argument rounds the number down to nearest 10 or 1000 etc

### BOOLEAN OPERATORS

# Quick, can you guess the value of this expression?

True or True and False

# To answer this, you'd need to figure out the order of operations.

# For example, and is evaluated before or. That's why the first expression above is True. If we evaluated it from left to right, we would have calculated True or True first (which is True), and then taken the and of that result with False, giving a final value of False.

# You could try to memorize the order of precedence, but a safer bet is to just use liberal parentheses. Not only does this help prevent bugs, it makes your intentions clearer to anyone who reads your code.

# IN SHORT - USE PARENTHESIS TO MAKE THINGS CLEAR FOR YOU AND OTHERS

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

print("BOOL 1",bool(1)) # all numbers are treated as true, except 0
print("BOOL 0",bool(0))
print("BOOL -1",bool(-1))

print("BOOL string",bool("asf")) # all strings are treated as true, except the empty string ""
print("BOOL empty string",bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"


def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# The key problem is that Python implictly parenthesizes the last part as:
# (not (rain_level > 0)) and is_workday
# Whereas what we were trying to express would look more like:

# not (rain_level > 0 and is_workday)

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

# CAN BE WRITTEN

# Try and think that when you see a < or >= or anything like that, that is RESOLVES TO TRUE OR FALSE
def concise_is_negative(number):
    return number < 0  # Your code goes here (try to keep it to one line!)

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return (not ketchup) and (not mustard) and (not onion)

# can be written 

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)


# calling integer on bool
print(int(True)) # 1
print(int(False)) # 0

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1

# Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...

# return (ketchup + mustard + onion) == 1

# Python implicity converts bool to integers when you use mathematical operators

### LISTS AND THEIR OPERATIONS

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets)
print(planets[-2]) # 'Uranus'
#SLICE 
print(planets[0:3]) # ['Mercury', 'Venus', 'Earth']

# the starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

print(planets[:3]) # ['Mercury', 'Venus', 'Earth']
# If I leave out the end index, it's assumed to be the length of the list.

print(planets[3:]) # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# All the planets except the first and last
print(planets[1:-1]) # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']

print(planets[-3:]) # ['Saturn', 'Uranus', 'Neptune'])

# Changing lists
# Lists are "mutable", meaning they can be modified "in place".

# One way to modify a list is to assign to an index or slice expression.

# For example, let's say we want to rename Mars:

planets[3] = 'Malacandra'

print(planets) #['Mercury', 'Venus' ,'Earth','Malacandra','Jupiter','Saturn','Uranus','Neptune']

# Hm, that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.

planets[:3] = ['Mur', 'Vee', 'Ur']
print("HERE", planets) # ['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

print(planets) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

len(planets) #8

# sorted returns a sorted version of a list:
sorted(planets) # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
# sum does what you might expect:
primes = [2, 3, 5, 7]
sum(primes) # 17
#We've previously used the min and max to get the minimum or maximum of several arguments. But we can also pass in a single list argument.
max(primes) # 7

### OBJECTS

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag) # 0
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag) # 3.0

### methods and attributes

# The things an object carries around can also include functions. A function attached to an object is called a method. (Non-function things attached to an object, such as imag, are called attributes).

# For example, numbers have a method called bit_length. Again, we access it using dot syntax:

x.bit_length # <function int.bit_length()>
# To actually call it, we add parentheses:
x.bit_length() # 4
# help(x.bit_length)
# The examples above were utterly obscure. None of the types of objects we've looked at so far (numbers, functions, booleans) have attributes or methods you're likely ever to use.

# But it turns out that lists have several methods which you'll use all the time.

### List methods

planets.append('Pluto')
print(planets) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto]
boo = planets.pop()
print("POPPED", boo) # pluto

planets.index('Earth') # 2

print ("Earth" in planets) # True
print ("RAYMONDO" in planets) # False

### TUPLES - IMMUTABLE LISTS

# Tuples are almost exactly the same as lists. They differ in just two ways.
# 1: The syntax for creating them uses parentheses instead of square brackets
# 2: They cannot be modified (they are immutable).
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3 # equivalent to above

print(tuple1) # (1, 2, 3)
print(tuple2) # (1, 2, 3)

# Tuples are often used for functions that have multiple return values.
# For example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple:

x = 0.125
x.as_integer_ratio() # (1, 8)

# These multiple return values can be individually assigned as follows:

numerator, denominator = x.as_integer_ratio()
print(numerator) # 1
print(denominator) # 8
print(numerator / denominator) # 0.125

# hence this bullshit:
a = 1
b = 0
a, b = b, a
print(a, b) # 0 1

### LOOPS AND LISTS - FOR/RANGE ETC

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet, end=' ') # print all on same line Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product) #360

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')   

# HELLO

### RANGE

for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

### WHILE
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1

# 0 1 2 3 4 5 6 7 8 9 

### LIST COMPREHENSION ********

squares = [n**2 for n in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# SAME THING WITHOUT LIST COMPREHENSION
squares = []
for n in range(10):
    squares.append(n**2)
squares

# MORE LIST COMPREHENSIONS

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets) # ['Venus', 'Earth', 'Mars']

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets) # ['VENUS!', 'EARTH!', 'MARS!']

# it's like [TRANSFORMATION TO BE APPLIED TO ITEM IN LIST THAT MEETS CONDITION for ITERABLE ITEM in LIST if CONDITION FOR APPLYING TRANSFORMATION]

# EG

thirtyTwos = [32 for planet in planets]
print(thirtyTwos) # [32, 32, 32, 32, 32, 32, 32, 32]

onlyHome = ["HOME!" for planet in planets if planet == "Earth"]
print(onlyHome) # ['HOME!']

homeWithNotHome = ["HOME!" if planet == "Earth" else "not home" for planet in planets ]
print(homeWithNotHome) # ['not home', 'not home', 'HOME!', 'not home', 'not home', 'not home', 'not home', 'not home']

homeWithOther = ["HOME!" if planet == "Earth" else planet for planet in planets]
print(homeWithOther) # ['Mercury', 'Venus', 'HOME!', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# WAY MORE EFFICIENT

def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative

# can be refuced to: 

def count_negatives(nums):
    return len([num for num in nums if num < 0])

# or even shorter:

def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])

def has_lucky_number(nums):
    print([num % 7 == 0 for num in nums])
    return any([num % 7 == 0 for num in nums])

has_lucky_number([3, 11, 21, 9])


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [num > thresh for num in L]


### STRINGS

hello = "hello\nworld"
print(hello) 

# hello
# world

# In addition, Python's triple quote syntax for strings lets us include newlines literally (i.e. by just hitting 'Enter' on our keyboard, rather than using the special '\n' sequence). We've already seen this in the docstrings we use to document our functions, but we can use them anywhere we want to define a string.

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello # True

# The print() function automatically adds a newline character unless we specify a value for the keyword argument end other than the default value of '\n':

print("hello")
print("world")
print("hello", end='')
print("pluto", end='') # hellopluto

planet = 'Pluto'
planet[0] #'P'
# Slicing
planet[-3:] #'uto'
# How long is this string?
len(planet) # 5
# Yes, we can even loop over them
[char+'! ' for char in planet] # ['P! ', 'l! ', 'u! ', 't! ', 'o! ']

### HOWEVER STRINGS DIFFER FROM LISTS IN THAT THEY ARE IMMMUTABLE
# cannot change or append

### String methods

claim = "Pluto is a planet!"
claim.upper() # 'PLUTO IS A PLANET!'
claim.lower() # 'pluto is a planet!'
# Searching for the first index of a substring
claim.index('plan') # 11
claim.startswith(planet) # True
# false because of missing exclamation mark
claim.endswith('planet') # False
#Going between strings and lists: .split() and .join()

# str.split() 
# turns a string into a list of smaller strings, breaking on whitespace by default. This is super useful for taking you from one big string to a list of words.
words = claim.split()
print (words) #['Pluto', 'is', 'a', 'planet!']
# Occasionally you'll want to split on something other than whitespace:
datestr = '1956-01-31'
year, month, day = datestr.split('-')

# str.join() 
#takes us in the other direction, sewing a list of strings up into one long string, using the string it was called on as a separator.
'/'.join([month, day, year]) # '01/31/1956'
# Yes, we can put unicode characters right in our string literals :)
' 👏 '.join([word.upper() for word in words]) # 'PLUTO 👏 IS 👏 A 👏 PLANET!'

# help(str.join)
print(" ".join(["Ray", "is", "awesome"])) # Ray is awesome

# stringify an intiger

print(type(str(9))) # 'str'

### INTERPOLATION with .format()

planet = 'Pluto'
position = 9

print(planet + ", you'll always be the " + str(position) + "th planet to me.")
# "Pluto, you'll always be the 9th planet to me."

# but this looks horibbly messy
# str.format() can help

print("{}, you'll always be the {}th planet to me.".format(planet, position))
# Pluto, you'll always be the 9th planet to me.

# So much cleaner! We call .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.

# Notice how we didn't even have to call str() to convert position from an int. format() takes care of that for us.

# If that was all that format() did, it would still be incredibly useful. But as it turns out, it can do a lot more. Here's just a taste:

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
# 2 decimal points, 3 decimal points, format as percent, separate with commas
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format( planet, pluto_mass, pluto_mass / earth_mass, population,)
#"Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

# Pluto's a planet.
# No, it's a dwarf planet.
# planet!
# dwarf planet!

### DICTIONARIES!!!!!!!!

numbers = {'one':1, 'two':2, 'three':3}
# Values are accessed via square bracket syntax similar to indexing into lists and strings.

print(numbers['one']) # 1
# print(numbers.one) # error

# We can use the same syntax to add another key, value pair
numbers['eleven'] = 11
print(numbers) # {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}

numbers['one'] = 'Pluto'
print(numbers) # {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}

### DICTIONARY COMPREHENSIONS

# Python has dictionary comprehensions with a syntax similar to the list comprehensions we saw in the previous tutorial.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

# {'Mercury': 'M',
#  'Venus': 'V',
#  'Earth': 'E',
#  'Mars': 'M',
#  'Jupiter': 'J',
#  'Saturn': 'S',
#  'Uranus': 'U',
#  'Neptune': 'N'}

# The in operator tells us whether something is a key in the dictionary

'Saturn' in planet_to_initial # True
'Betelgeuse' in planet_to_initial # False
 
# ITERATING OVER DICTIONARIES

numbers = {'one':1, 'two':2, 'three':3}

for k in numbers:
    print(k)

# one
# two
# three

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# where the iterable k is the key 

# one = Pluto
# two = 2
# three = 3
# eleven = 11

# We can access a collection of all the keys or all the values with dict.keys() and dict.values(), respectively.
numbers = {'one':1, 'two':2, 'three':3}

print(numbers.keys()) # dict_keys(['one', 'two', 'three'])
print(numbers.values()) # dict_values([1, 2, 3])

# THESE ARE NOT SUBSCRIPTABLE - CANNOT INDEX INTO THEM AS DICTS NON INDEXED DUH

planet_to_initial = {'Mercury': 'M',
 'Venus': 'V',
 'Earth': 'E',
 'Mars': 'M',
 'Jupiter': 'J',
 'Saturn': 'S',
 'Uranus': 'U',
 'Neptune': 'N'}

print(' '.join(sorted(planet_to_initial.values()))) # E J M M N S U V

# The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. (In Python jargon, an item refers to a key, value pair)

print(planet_to_initial.items()) # dict_items([('Mercury', 'M'), ('Venus', 'V'), ('Earth', 'E'), ('Mars', 'M'), ('Jupiter', 'J'), ('Saturn', 'S'), ('Uranus', 'U'), ('Neptune', 'N')])

# print(planet_to_initial.items()[0]) # not subscribtable

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet, initial))

# Mars begins with "M"
# Jupiter begins with "J"
# Saturn begins with "S"
# Uranus begins with "U"
# Neptune begins with "N" ...

# see all dict methods with help(dict)
# help(str)

def word_search(doc_list, keyword):
    print("NEW EXANPLE")
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    indexes = []

    docListLowerCase = [doc.lower() for doc in doc_list]
    for index, string in enumerate(docListLowerCase):
        listOfWordsInString = string.split()
        listOfWordsInString = [word.strip("?,.") for word in listOfWordsInString]
        if any([word == keyword for word in listOfWordsInString]):
            indexes.append(index)
    
    print("ENDING")
    print(indexes)

    return indexes

# solution
def word_search(doc_list, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        words = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [word.rstrip('.,').lower() for word in words]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

### EXTERNAL LIBRARIES

import math
import math as mt




print("It's math! It has type {}".format(type(math))) # It's math! It has type <class 'module'>

# math is a module. A module is just a collection of variables (a namespace, if you like) defined by someone else. We can see all the names in math using the built-in function dir()

print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))
# pi to 4 significant digits = 3.142

# But most of what we'll find in the module are functions, like math.log:

math.log(32, 2) # 5.0

# help(math.log)
from math import *

# when you import with the above syntax you import all of the variable from math and you can use them without the math... prefix eh instead of math.pi and math.log(32, 2) you can go:

print(pi) # 3.141592653589793
print(log(32, 2)) # 5

# but this is not advised as it's less clear
### submodules 

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...", dir(numpy.random)[-15:])

# numpy.random is a <class 'module'>
# it contains names such as... ['seed', 'set_state', 'shuffle', 'standard_cauchy', 'standard_exponential', 'standard_gamma', 'standard_normal', 'standard_t', 'test', 'triangular', 'uniform', 'vonmises', 'wald', 'weibull', 'zipf']

# So if we import numpy as above, then calling a function in the random "submodule" will require two dots.
# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls) # array([4, 2, 4, 5, 3, 1, 4, 2, 5, 1])

### TOOLS FOR HOW TO WORK WITH NEW STRANGE TYPES

# 1. type(strangeThing) -> what type of thing is it
# 2. dir(strangeThing) -> what can I do with it
# 3. help(strangeThing) -> wtf I need to know more

# E.G.

print(type(rolls)) # numpy.ndarray
print(dir(rolls)) 
# ['T', '__abs__', '__add__', '__and__', '__array__', '__array_finalize__', '__array_function__', '__array_interface__', '__array_prepare__', '__array_priority__', '__array_struct__', '__array_ufunc__', '__array_wrap__', '__bool__', '__class__', '__complex__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__ilshift__', '__imatmul__', '__imod__', '__imul__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__ior__', '__ipow__', '__irshift__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lshift__', '__lt__', '__matmul__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__xor__', 'all', 'any', 'argmax', 'argmin', 'argpartition', 'argsort', 'astype', 'base', 'byteswap', 'choose', 'clip', 'compress', 'conj', 'conjugate', 'copy', 'ctypes', 'cumprod', 'cumsum', 'data', 'diagonal', 'dot', 'dtype', 'dump', 'dumps', 'fill', 'flags', 'flat', 'flatten', 'getfield', 'imag', 'item', 'itemset', 'itemsize', 'max', 'mean', 'min', 'nbytes', 'ndim', 'newbyteorder', 'nonzero', 'partition', 'prod', 'ptp', 'put', 'ravel', 'real', 'repeat', 'reshape', 'resize', 'round', 'searchsorted', 'setfield', 'setflags', 'shape', 'size', 'sort', 'squeeze', 'std', 'strides', 'sum', 'swapaxes', 'take', 'tobytes', 'tofile', 'tolist', 'tostring', 'trace', 'transpose', 'var', 'view']

print(rolls.mean()) # 3.1

print(rolls.tolist()) # [4, 2, 4, 5, 3, 1, 4, 2, 5, 1]

help(rolls.ravel)

# Help on built-in function ravel:

# ravel(...) method of numpy.ndarray instance
#     a.ravel([order])
    
#     Return a flattened array.
    
#     Refer to `numpy.ravel` for full documentation.
    
#     See Also
#     --------
#     numpy.ravel : equivalent function
    
#     ndarray.flat : a flat iterator on the array.

# NUMPY ARRAYS AND LISTS ARE NOTTTTT THE SAME

[3, 4, 1, 2, 2, 1] + 10 # ERRORS

rolls + 10 # array([14, 12, 14, 15, 13, 11, 14, 12, 15, 11])

xlist = [[1,2,3],[2,4,6],]
print(xlist) # xlist = [[1, 2, 3], [2, 4, 6]]
x = numpy.asarray(xlist)
print(x) 
# x =
# [[1 2 3]
#  [2 4 6]]

# Get the last element of the second row of our numpy array
x[1,-1] # 6

# Get the last element of the second sublist of our nested list?
xlist[1,-1] # ERROR NEEDS TO BE xlist[1][-1]

### WHAT ARE THOSE DUNDER METHODS "__add__", "__class__", "__contains__" etc

# When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, names that follow this double-underscore format have a special meaning to Python.

# So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes. It's equivalent to (the much uglier) [1, 2, 3].__contains__(x).


