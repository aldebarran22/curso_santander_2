"""
Calcular la intersección y la unión de dos listas.
"""

L1 = [1,3,5,6,3,3,1,5,6,9]
L2 = [1,2,3,5,5,8,10]

inter = []
for i in L1:
    if i in L2 and i not in inter:
        inter += [i]
print(inter)

union = []
for i in L1+L2:
    if i not in union:
        union += [i]
print(union)        
