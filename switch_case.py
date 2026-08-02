x= int(input("Enter the value of x:"))
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4 if x<100:
        print("x is smaller than 100")
    case _ if x!=50:
        print(x,"x is  not 50")