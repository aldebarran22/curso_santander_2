"""
Simular el comportamiento de un cajero automático

importe:>33
Importe incorrecto

importe:>RR
Importe incorrecto

importe:>230
4 de 50
1 de 20
1 de 10

importe:>
"""

def main():
    tipos_billetes = [10,20,50]
    tipos_billetes.sort(reverse=True)
    min_billete = min(tipos_billetes)

    while True:
        importe = int(input('Importe:> '))
        if importe % min_billete != 0:
            print('Importe debe ser múltiplo de 10')

        else:
            # Desglose de billetes
            billetes = dict()

            for b in tipos_billetes:
                if importe >= b:
                    billetes[b] = importe // b
                    importe %= b

                if importe == 0: break

            for b,cuenta in billetes.items():
                print(f"{cuenta} de {b}")
            print()

if __name__ == '__main__':
    main()