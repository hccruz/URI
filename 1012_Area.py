valores = input()

l1 = valores.split(" ")

A = float(l1[0])
B = float(l1[1])
C = float(l1[2])

triangulo = (A * C) / 2
circulo = C**2 * 3.14159
trapezio = ((A + B) * C) / 2
quadrado = B**2
retangulo = A * B

print(triangulo)
print(circulo)
print(trapezio)
print(quadrado)
print(retangulo)
