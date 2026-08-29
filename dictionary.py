#Printing Dictionaries
disc={"pratyush":34,"ayush":45,"ankit":55,"amit":65}
print(disc)
#Accessing Dict.
#1.single value
print(disc["pratyush"])
print(disc.get("pratyush"))#it does not through an error even when the key does not exist
#2.Accessing whole dict.
print(disc)
#3.Accessing multiple values
print(disc.values()) # for values
print(disc.keys()) # for keys
#or
for x in disc.keys(): # for keys
    print(x)
#for values
for x in disc.keys():# for values
    print(disc[x])
#or
disc={"pratyush":34,"ayush":45,"ankit":55,"amit":65} # for both togather
for x in disc.keys():
    print(f"i am {x} and i am {disc[x]} year old")
#4.Accessing key-value pairs
disc={"pratyush":34,"ayush":45,"ankit":55,"amit":65} # for both togather
print(disc.items())
#or
for key,value in disc.items():
    print(f"i am {key} and i am {value} year old")
