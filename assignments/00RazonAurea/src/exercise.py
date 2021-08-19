import math

def main():
    #escribe tu código abajo de esta línea
 
    numero = float(input('Número: '))
    decimales = int(input('Decimales a mostrar: '))

    phi = (1+math.sqrt(5))/2
    aurea = round(numero*phi,decimales)

    print(f'Razón áurea: {aurea}')




if __name__ == '__main__':
    main()
