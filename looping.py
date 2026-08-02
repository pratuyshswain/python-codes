#1 for loop
#iterating over a String
name="Pratyusha swain"
for i in name:#Here (i) mean every index in the word Pratyusha Swain
    print(i)
# #iterating over a list
colours=["red","green","blue","yellow"]
for I in colours:
    print(i)
    for x in i:
        print(x)
# #example of stop
 #range() function
for  i in range(22):#prints 0-->21
    print(i)
# #example of (start , stop)
for  i in range(2,22):#prints 2-->21
    print(i)
# #example of (start ,stop ,step)
for i in list(range(2 ,11 ,2)):
    print(i)
#2 While loop
#ex for even no 0 to10
i=0
while i<=10:
    print(i)
    i=i+2
# ex with user input
i=int(input("Enter a number to start with: "))
while i<=10:
    print(i)
    i=i+1
# print("End of loop")
#decrementing loop
#ex 2
i=10
while i>10:
    print(i)
    i=i-1
#else with while loop
count =5
while count > 0:
    print(count)
    count = count - 1
else:
    print("Goodbye")
