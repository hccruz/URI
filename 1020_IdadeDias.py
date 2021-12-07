N = int(input())

ano = N // 365
resto = N % 365

mes = resto // 30

dia = resto % 30

print(str(ano) + " ano(s)")
print(str(mes) + " mes(es)")
print(str(dia) + " dia(s)")
