valor = int(input())

notas = [100, 50, 20, 10, 5, 2 ,1]

quantidades = []

for nota in notas:
    quant = valor // nota
    quantidades.append(quant)
    valor = valor % nota

for i in range(len(quantidades)):
    print(str(quantidades[i]) + " notas(s) de R$ " + str(notas[i]) +",00")
