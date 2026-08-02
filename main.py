#this is a single line comment in python
"""This is a multiline comment in
python"""
'''this also a multiline comment in python'''
#Escape sequence character
print("hey i am a good boy and\n also you")
print("hey i am a \"good boy\"\n and also you")
#parameter
print("pratyusha",6,7,sep="~")
print("pratyusha", 6 ,7,end="033\n")
print("pratyusha", 6 ,7,end="033")
#tuple
tuple1=(("parrot","sparrow"),("lion","tiger"))
print(tuple1)
#mapped data
dict1= {"name":"sparrow","age":"2"}
print(dict1)
#user input
a=input()
print("my name is ",a)
#or
a=input("enter your name : ")
print("my name is :",a)
#string
name="pratyush"
print(name[0])
#Looping in string
name="pratyush"
for characters in name:
 print(characters)
#length in string
sentence="my name is Pratyusha swain"
length = len(sentence)
print(length)
pie="ApplePie"
print(pie[0:5])
#in negative limit
pie="ApplePie"
print(pie[0:-3])#form 0 to len(pie)-3
print(pie[-3:-1])#from len(pie)-3 to len(pie)-1
