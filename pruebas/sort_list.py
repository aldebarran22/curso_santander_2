# ordenar listas:

def compara(a):
	return len(a)
		
		
L=["zz","aa","bgkggkgk","696959","r","556"]
print(L)

L.sort()
print(L)
print(sorted(L, key=compara))	

s = "This is a test string from Andrew"	
L = s.split(" ")
L.sort(key=len)
print(L)


LL=L.copy()
L[0]=9999999999
print("LL:",LL)
print("L:",L)

