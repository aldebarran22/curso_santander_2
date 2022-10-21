# funciones:
def imprimir(s, veces=1):
	print(s*veces)

def varios(p1,p2,*p):
	for val in p:
		print(val)

def otros(p1,p2,**otros):
	for i in otros.items():
		print(i)
		
		
def f(x, y): 
	x = x + 3 
	y.append(23) 
	print(x, y)
	
	
x=22
y=[22]
f(x,y)
print(x,y)	

	
imprimir("hola")
imprimir("adios",5)

varios(1,2,3,4,5)
varios(1,2)	


otros(1,2,tres=3,cuatro=4)
