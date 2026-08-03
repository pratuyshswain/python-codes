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

#ex
def greet_user(name,age):
    print("Hello, " + name + "!")
    print(age, "years old!")
greet_user("Alice",20)