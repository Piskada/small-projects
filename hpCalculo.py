# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hp = sqrt(co ** 2 + ca ** 2)
print(f"O comprimento da hipotenusa é: {hp:.2f}")
print('=' * 50)
print('\n')
print('=' * 50)
co1 = float(input("Digite o comprimento do cateto oposto: "))
ca1 = float(input("Digite o comprimento do cateto adjacente: "))
hp1 = hypot(co1, ca1)
print(f"O comprimento da hipotenusa de outra forma é: {hp1:.2f}")