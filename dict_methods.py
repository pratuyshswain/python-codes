#dictionary methods
#1.update()
dicti_1={"a":1,"b":2,"c":3,"d":4,"e":5}
dicti_2={"a":9,"b":8,"t":3,"f":4}
dicti_1.update(dicti_2)
print(dicti_1)
dicti_1.update(dicti_2)
#2.clear()
dicti_1.clear()
print(dicti_1)
#3.pop()
dicti_2.pop("a")
print(dicti_2)
#4.popitems()
dicti_1={"a":1,"b":2,"c":3,"d":4,"e":5}
dicti_1.popitem()
print(dicti_1)
#5.del
dicti_1={"a":1,"b":2,"c":3,"d":4,"e":5}
del dicti_1["d"]
print(dicti_1)
#6.clrear()
dicti_1={"a":1,"b":2,"c":3,"d":4,"e":5}
dicti_1.clear()
print(dicti_1)
#7.copy()
prices = {'apple': 10, 'banana': 5}
new_prices = prices.copy()
new_prices['apple'] = 15
print("Original:", prices)
print("Copy:    ", new_prices)