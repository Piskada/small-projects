import random

acertos = 0
resposta_dos_competidores = []



t = int(input('Digite o chá que foi dado aos competidores: 1 - chá branco, 2 - chá verde, 3 - chá preto, 4 - chá de ervas: '))

for i in range(1, 6):
    resposta = random.randint(1, 4)
    resposta_dos_competidores.append(resposta)
    if resposta == t:
        acertos += 1

print(t)
print(resposta_dos_competidores)
print(acertos)
