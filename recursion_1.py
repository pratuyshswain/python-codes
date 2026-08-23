#factorial(5)=5*factorial(4) return
#factorial(4)=4*factorial(3) return
#factorial(3)=3*factorial(2) return
#factorial(2)=2*factorial(1) return
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
#ex-2
def countdown(count):
    # 1. The Base Case (The Stopping Point)
    if count == 0:
        print("Liftoff! 🚀")
        return  # This tells the function to completely stop

    # 2. The Recursive Case (The Work)
    print(count)
    countdown(count - 1)  # The function calls ITSELF, but with a smaller
print(countdown(7))

# f(0)=o                          =0
# f(1)=1                          =1
# f(2)=f(1)+f(0)                  =1
# f(3)=f(2)+f(1)                  =2
# f(4)=f(3)+f(2)                  =3
# f(n)=f(n-1)+f(n-2)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))
#or using iteration
def fibonacci(n):
    if n == 0:
        return 0
    a,b = 0,1
    for _ in range(2,n+1):
        a,b =b,a+b
    return b
print(fibonacci(3))

