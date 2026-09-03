set_1={"car",1,1,104,35,"cat"}
print(set_1)
#for accessing elements from the set
for x in set_1:
    print(x)
# set methods()
#1.union()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
print(set_3.union(set_2))
#2.update()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_3.update(set_2)
print(set_3)
#3.intersection()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_4=set_3.intersection(set_2)
print(set_4)
#4.intersection_update()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_3.intersection_update(set_2)
print(set_3)
#5.symmetric_difference()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_4=set_3.symmetric_difference(set_2)
print(set_4)
#6.symetric_difference_update()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_3.symmetric_difference_update(set_2)
print(set_3)
#7.difference()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_4=set_3.difference(set_2)
print(set_4)
#8.difference_update()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
set_3.difference_update(set_2)
print(set_3)
#9.isdisjoint()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g","h","i","j"}
print(set_2.isdisjoint(set_3))
#10.issuperset()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g"}
print(set_2.issuperset(set_3))
#11.issubset()
set_2={"a","b","c","d","e","f","g"}
set_3={"e","f","g"}
print(set_3.issubset(set_2))
#12.add()
set_2={"a","b","c","d","e","f","g"}
set_2.add("z")
print(set_2)
#13.remove()
set_2={"a","b","c","d","e","f","g"}
set_2.remove("a")
print(set_2)
#14.dicard()
set_2={"a","b","c","d","e","f","g"}
set_2.discard("g")
print(set_2)
#15.pop()
set_2={"a","b","c","d","e","f","g"}
item=set_2.pop()
print(item)
print(set_2)
#16.del
set_2={"a","b","c","d","e","f","g"}
del set_2
#17.clear()
set_2={"a","b","c","d","e","f","g"}
set_2.clear()
print(set_2)
#numerator()
#denominator()
#18.search items
set_2={"a","b","c","d","e","f","g"}
if "a" in set_2:
    print("a is present")
else:
    print("a is not present")
#set iteration
num={1,2,3,5,6,}
for x in num:
    print(x)
#set comprehension
squares={2**x for x in range(10,19)}
print(squares)