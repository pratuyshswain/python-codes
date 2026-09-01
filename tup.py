#tuple
#1. Using Parentheses ()
colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = (1, [2, 3], (4, 5, 6))
#2. Without Parentheses (Comma-Separated)
also_numbers = 1, 2, 3, 4, 5
#3. Using the tuple() Constructor
new_tuple = tuple(("apple", "banana", "cherry")) # use double brackets
list_items = ["x", "y", "z"] # Creating a tuple from a list
tuple_items = tuple(list_items) # ('x', 'y', 'z’)
#4. Single-Item Tuple
tuples_single = ("only",)
print(type(also_numbers))
print(new_tuple)
#repetition
tup=("hello",)*3
print(tup)
#Checking in tuple
numbers = (10, 20, 30, 40)
print(20 in numbers) # Output: True
#or
numbers = (10, 20, 30, 40)
if 20 in numbers:
    print(20 in numbers)
# iterating over tuple Example:
fruits = ("apple", "mango", "cherry")
# Using for loop
for xe in fruits:
 print(xe)
#using while loop
fruits = ("apple", "mango", "cherry")
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
#tuple methods()
#count method()
fruits = ("apple", "mango", "cherry")
print(fruits.count("apple"))
#index method()
print(fruits.index("mango"))
#as_integer_ratio()returns two nums in (x,y)where x/y is a
a = 0.5
print(a.as_integer_ratio())
#packing items in a tuple
a = "Madhav"
b = 21
c = "Engineer"
pack_tuple = a,b,c # Packing values into a tuple
print(pack_tuple)
#unpacking a tuple
a,b,c=pack_tuple
print(a)
print(b)
print(c)
