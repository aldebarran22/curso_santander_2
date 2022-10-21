# control de flujo:

dia = 10
if 0 < dia < 16:
	print("en el intervalo")

while True: 
	entrada = input("> ") 
	if entrada == "adios": 
		break 
	else: 
		print(entrada)



i=0
while i < 10:
	print(i,end="")
	i+=1
else:
	print("fin de bucle")
