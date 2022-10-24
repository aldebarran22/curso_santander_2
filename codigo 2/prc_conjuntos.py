"""
Resolver con conjuntos las siguientes preguntas:
"""
comida = {'Ana','Fernando','Miguel','Olga','Sandra'}
cena = {'Fernando','Miguel','Raquel','Sandra','Raul'}

print('Quien va a solo a comer:', comida - cena)
print('Quien va solo a un evento:', comida ^ cena)
print('Quien va a comer y a cenar:', comida & cena)
print('Quienes han participado en los eventos:', comida | cena)

