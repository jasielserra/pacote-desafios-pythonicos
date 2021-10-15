def imprimir_triangulo_de_numeros(n: int):
    for i in range(1, n + 1):
        for x in range(i):
            print(x, end=' ')
        print(" :")

print('Triangulo com 7')
imprimir_triangulo_de_numeros(7)

print('Triangulo com 4')
imprimir_triangulo_de_numeros(4)