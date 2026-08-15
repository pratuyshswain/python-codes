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
#list.index
colours=["blue","red","green","orange","yellow","purple","pink","brown"]
print(colours.index("yellow"))
#list.count
l=[1,2,3,4,5,10,7,8,11,1,1]
print(l.count(1))
#list.copy
lis=[1,2,3,4,5,6,7,9]
new_lis=lis.copy()
print(new_lis)
#list.insert()
animals=["cow","tiger","monkey","dog","cat"]
animals.insert(0,"pig")
print(animals)
#list.extend
animal=["cow","tiger","monkey","dog","cat"]
colours=["blue","red","green","orange","yellow","purple","pink","brown"]
animal.extend(colours)
print(animal)
#list.remove()
animal=["cow","tiger","monkey","dog","cat"]
animal.remove("cow")
print(animal)
#list.pop()
fruits = ["apple", "banana", "cherry"]
snack = fruits.pop(1)
print(fruits)
print(snack)
#list.clear()
animal=["cow","tiger","monkey","dog","cat"]
animal.clear()
print(animal)

