# binario, octal y hex.

# enteros en octal:
un_octal = 0o27
print("octal: ", un_octal)


# enteros en hexadecimal:
un_hx = 0xFF
print("un Hx ", un_hx)

x = 255
print("Binario:",bin(x))
print("Octal:",oct(x))
print("Hx: ",hex(x))

print(int('4d2', 16))
print(int('10011010010', 2))

x = None
print(x)
if x:
	print("x es True")
else:
	print("x es false")



