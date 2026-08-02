a=int(input("enter a number:"))                #user input
b=int(input("enter another number:"))

def isGreater(a,b):                 #user defined function
    if (a>b):
        print(a ,"is greater than",b)
    elif(a==b):
        print(a,"is equal to",b)
    else:
        print(b ,"is greater than ",a)
def isLesser(a,b):
    if (a<b):
        print(a," is less than ",b)
    elif(a==b):
        print(a,"is equal to  ",b)
    else:
        print(b," is less than ",a)
isGreater(a,b)                                              #function calling
isLesser(a,b)