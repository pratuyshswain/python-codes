#if else statement
#sequence is if->elif->...->(if->elif->...->else)->else
#ex-1
num=int(input("Enter a number:"))
if(num==0):
     print("it is special")
elif(num>=0):
    if(num>=1000):
        print("you have reached limit of calculation")
    elif(num%2==0):
        print("it is even")
    else:
        print("odd")
else:
     print("negative")
 #ex-2
num=int(input("Enter a number:"))
if(num<0):
    print("No. is negative")
elif(num>0):
    if( num>=0 and num<=10):
        print("The number is in between1-10")
    elif(num>10 and num<=20):
        print("The number is in between10-20")
    else:
        print("The no is greater than 20")
else:
    print("The no is zero")