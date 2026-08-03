a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def isGreater(a, b):#here def is built in and isGreater is userdefined
    if a > b:
        print(a,"is greater than ",b)
    else:
        print(b,"is greater than ",a)
isGreater(a,b)
#if no argument is under the function
def islesser(a, b):
    pass                #so it skips the function

#ex--1
def greet_user(name,age):
    print("Hello, " + name + "!")
    print(age, "years old!")
greet_user("Alice",20)
#--2
def add_numbers(num1, num2):
 total = num1 + num2
 return total
add_numbers(5,10)   #calling part
