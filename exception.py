a=input("Enter the number : ")
print(f"Multiplication table of {a}is :")
try:

    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
    print(e)
    print("Try integer as input")
#specific type of error handling
#ex-1
a=input("Enter the number : ")
print(f"Multiplication table of {a}is :")
try:

    for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except ValueError:
    print("Try integer as input")
#ex-2
try:
    num=int(input("Enter an integer : "))
    a=[6,3]
    print(a[num])
except IndexError:
    print("Try integer as input")







