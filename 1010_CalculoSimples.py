# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

Peca1 = input()
Peca2 = input()

l1 = Peca1.split(" ")
l2 = Peca2.split(" ")

quant1 = int(l1[1])
valor1 = float(l1[2])

quant2 = int(l2[1])
valor2 = float(l2[2])

valorpago = quant1 * valor1 + quant2 * valor2

print("VALOR A PAGAR: R$ %.2f" %valorpago)
