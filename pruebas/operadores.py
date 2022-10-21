# operadores:
x = 9
y = 2
print(x//y)

# logicos:
x = (True, True, False, False)
y = (True, False, True, False)

print("AND")
for i in range(len(x)):
	print(x[i],"\t",y[i],"\t",x[i] & y[i])
	
print("\nOR")
for i in range(len(x)):
	print(x[i],"\t",y[i],"\t",x[i] | y[i])

print("\nXOR")
for i in range(len(x)):
	print(x[i],"\t",y[i],"\t",x[i] ^ y[i])
