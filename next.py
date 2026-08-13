#list methods
#1. list.sort()
#ex=1
l=[1,2,3,4,5,10,7,8]
l.sort()
print(l)
#ex=2 for decending order
l=[1,32,3,4,5,10,7,8]
l.sort(reverse=True)
print(l)
#ex=3
colours=["blue","red","green","orange","yellow","purple","pink","brown"]
colours.sort()
print(colours)
#2. list.reverse()
l=[1,2,3,4,5,10,7,8]
l.reverse()
print(l)
#3. list.index()
colours=["blue","red","green","orange","yellow","purple","pink","brown"]
print(colours.index("red"))
