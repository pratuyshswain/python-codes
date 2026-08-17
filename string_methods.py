#string methods
#1.upper()
a="   Pratyush  "
print(a.upper())
#2.lower()
print(a.lower())
#3.strip()
print(a.strip())    #it removes the ___Pratyush___ spaces
#4.rstrip()
b="BBRRR"
print(b.rstrip("R"))# only removes characters from rightside of the string
#5.replace()
str="silver spoon"
print(str.replace("sp","H"))
#6.split()
#ex-1
ptr_2="dog cat cow"
print(ptr_2.split(" "))
#ex-2
ct="A*B*C"
print(ct.split("*"))
#7.capitalize
blog=("i have a dog")
print(blog.capitalize())
#8.center()
ctr="welcome"
print(ctr.center(10))
#9.count()
str_2="ppratyush"
print(str_2.count("p"))
#10.endswith()
ctr="welcome to the park"
print(ctr.endswith("to",2,10))


