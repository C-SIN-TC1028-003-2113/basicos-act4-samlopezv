import math
def main():
    #escribe tu código abajo de esta línea
    a= float(input('Area a pintar en metros: '))
    r = float(input('Rendimiento (m2/L): '))

    li= int(math.ceil (a/r))

    print(f'Litros a comprar: {li}')

if __name__ == '__main__':
    main()
