numeros = input().split(" ")

A, B, C = numeros

MaiorAB = (int(A) + int(B) + abs(int(A) - int(B))) / 2

MaiorABC = (MaiorAB + int(C) + abs(MaiorAB - int(C))) / 2

print("%d eh o maior" %MaiorABC)
