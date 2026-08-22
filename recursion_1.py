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
#Fibonacci series
#formula:
# f(0)=o
# f(1)=1
# f(2)=f(1)+f(2)
# f(3)=f(3)+f(3)
# f(4)=f(4)+f(4)
# f(n)=f(n-1)+f(n-2)
def countdown(count):
    # 1. The Base Case (The Stopping Point)
    if count == 0:
        print("Liftoff! 🚀")
        return  # This tells the function to completely stop

    # 2. The Recursive Case (The Work)
    print(count)
    countdown(count - 1)  # The function calls ITSELF, but with a smaller
print(countdown(7))