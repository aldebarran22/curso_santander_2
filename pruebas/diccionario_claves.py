# prueba claves de diccionario:

d = {"AA":1,"BB":2, "CC":3}

for k,v in d:
	print(k,v)

if "AA" in d:
	print("existe")
else:
	print("No existe")
	
	
print(dict.fromkeys("ABC","123"))
print(dict.fromkeys([1,2,3,4,5],"123"))
print(type(d))
print(d.keys(), type(d.keys()), list(d.keys()))
print(d.values(), type(d.values()))
print(d.items(), type(d.items()))

print("\nkeys")
for k in d.keys():
	print(k)
print()

print("\nValues")
for k in d.values():
	print(k)
print()


print("\nitems")
for k in d.items():
	print(k)
print()

dd = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dd2=dd.copy()
print("popitem: ",dd2.popitem())
print("dd2",dd2)

del dd['Name']; # remove entry with key 'Name'
dd.clear()     # remove all entries in dict
print(dd)
#del dd ;        # delete entire dictionary

print ("dict['Age']: ", dd['Age'])
#print ("dict['School']: ", dd['School'])
