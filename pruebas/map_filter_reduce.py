# map filter reduce


# map
def cuadrado(a):
	return a**2
	
	
L=[1,2,3,4,5,6,7,8,9]
L2=list(map(cuadrado,L))
print(L2)
	
	
L3=[cuadrado(i) for i in L]
print(L3)


# filter

def es_par(n): 
	return (n % 2.0 == 0)

L = [1, 2, 3]
l2 = list(filter(es_par, L))
print(l2)

L2 =[i for i in L if i % 2 == 0]
print(L2)

# filter con lambda
L = [1, 2, 3]
L2 = list(filter(lambda n: n % 2.0 == 0, L))
print("lambda: ",L2)

# reduce
import functools

def sumar(x, y): 
	return x + y

l = [1, 2, 3]
l2 = functools.reduce(sumar, l)
print(l2)
