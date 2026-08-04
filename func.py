#def function
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
add_numbers(5,10)#calling part
result=add_numbers(5,10)
#ex--3
def calculate_score(Points,Bonus=0):
    total = Points + Bonus
    return total
calculate_score(100,50)
print(calculate_score(100,50))
#abs function
number=float(input("Enter a number:"))
if number>0:
    print(number)
elif number==0:
    print(number)
else:
    print(abs(number))
#min function
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)     #print the min value among the diff1,2,3
print(                                          # calling part
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists .
)
#Functions Applied to Functions

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)                              #mean mult_by_five(5)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))                                              #mean mult_by_five(mult_by_five(5))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n',
)# '\n' is the newline character - it starts a new line
# max function

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
#round function
def rounded_numbers(num):
    return round(num)
print(rounded_numbers(1.123456))
# with two decimal number right shift
def rounded_numbers(num):
    return round(num,2)
print(rounded_numbers(1.123456))
