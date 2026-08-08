#list
colours=["blue","red","green","orange"]
print(colours[-2])
#list slicing
numbers = [10, 20, 30, 40, 50, 60]
# Slice from index 1 to 3
print(numbers[1:4]) # Output: [20, 30, 40]
# Slice from start to index 2
print(numbers[:3]) # Output: [10, 20, 30]
# Slice all alternate elements
print(numbers[0::2]) # Output: [10, 30, 50]
# Slice with negative indices
print(numbers[-4:-1]) # Output: [30, 40, 50]
# Reverse list
print(numbers[::-1]) # Output: [60,50,40,30,20,10]
#modifying list
colours[2]="white"
print(colours)
#join list
list3=colours+numbers
print(list3)
#Flatten a Nested List - using List Comprehension
def flatten_list(lst):
 return [item for sublist in lst for item in sublist]
# Example
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = flatten_list(nested_list)
print(flattened)
# Output: [1, 2, 3, 4, 5, 6]
#Example: iterating over list
fruits = ["apple", "banana", "cherry"]
# Using for loop
for fruit in fruits:
 print(fruit)
# Using while loop
index = 0
while index < len(fruits):
 print(fruits[index])
 index += 1
