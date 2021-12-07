N = float(input())

nota100 = int(N // 100)
resto = N % 100

nota50 = int(resto // 50)
resto %= 50

nota20 = int(resto // 20)
resto %= 20

nota10 = int(resto // 10)
resto %= 10

nota5 = int(resto // 5)
resto %= 5

nota2 = int(resto // 2)
resto %= 2

moeda1 = int(resto // 1)
resto %= 1

moeda050 = int(resto // 0.50)
resto %= 0.50

moeda025 = int(resto // 0.25)
resto %= 0.25

moeda010 = int(resto // 0.10)
resto %= 0.10

moeda005 = int(resto // 0.05)
resto %= 0.05

moeda001 = int(resto // 0.01)

print("NOTAS:")
print(str(nota100) + " nota(s) de R$ 100.00")
print(str(nota50) + " nota(s) de R$ 50.00")
print(str(nota20) + " nota(s) de R$ 20.00")
print(str(nota10) + " nota(s) de R$ 10.00")
print(str(nota5) + " nota(s) de R$ 5.00")
print(str(nota2) + " nota(s) de R$ 2.00")
print("MOEDAS:")
print(str(moeda1) + " moeda(s) de R$ 1.00")
print(str(moeda050) + " moeda(s) de R$ 0.50")
print(str(moeda025) + " moeda(s) de R$ 0.25")
print(str(moeda010) + " moeda(s) de R$ 0.10")
print(str(moeda005) + " moeda(s) de R$ 0.05")
print(str(moeda001) + " moeda(s) de R$ 0.01")
