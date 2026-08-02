#break statement ex with user input
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search=input("Fruit name to search: ")


for fruit in fruits:
    print("Checking:", fruit)
    if fruit == search:
        print("Found the fruit",fruit)
        break
#break with nested loop
for outer_number in [1, 2]:
    for inner_letter in ['A', 'B', 'C']:
        if inner_letter == 'B':
            break
        print(outer_number, inner_letter)
#Continue statement
for number in range(1, 6):
    if number  == 3:
        continue
    print(number)
#do while loop in python using break statement
while True:
    number = int(input("Enter a number: "))
    print(number)
    if number == 0:
        break