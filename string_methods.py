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
#11.find()
sr="python is a coding language , it is not a snake "
print(sr.find("is"))
#12.index()
p="i have a cat"
print(p.index("cat"))
#13.isalnum()
A="Wellcome001"
print(A.isalnum())
#14.isalpha()
A="Wellcome001"
print(A.isalpha())
#15.islower()
A="wellcome"
print(A.islower())
#16.isupper()
a="WELLCOME"
print(a.isupper())
#17.isprintsble()
str6="wellcome\n"
print(str6.isprintable())  #returns false
# 18.isspace()
str4="  "
print(str4.isspace()) #return true
#19.istitle()
str5="There Is A Lion"
print(str5.istitle()) #returns true
#20.startswith()
prat="my name is Patrick"
print(prat.startswith("my name"))#returns true
#21.swapcase()
st21="Python Is A Language"
print(st21.swapcase())
#22.title
T="his name is dan and he has a cat"
print(T.title())
