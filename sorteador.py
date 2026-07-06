# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alunos = []
for i in range(1, 5):
    aluno = input(f"Digite o nome do {i}º aluno: ")
    alunos.append(aluno)

escolhido = random.choice(alunos)
print(f"O aluno que vai apagar o quadro vai ser o(a) {escolhido}")

