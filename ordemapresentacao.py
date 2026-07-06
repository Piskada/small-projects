#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
alunos = []
for i in range (1, 5):
    aluno = input(f"Digite o nome do {i}º aluno: ")
    alunos.append(aluno)

random.shuffle(alunos)
print(f"A ordem de apresentação será: {alunos}")
