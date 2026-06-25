import random

acertos = 0
resposta_dos_competidores = []



t = random.randint(1, 4)

for i in range(1, 6):
    resposta = random.randint(1, 4)
    resposta_dos_competidores.append(resposta)
    if resposta == t:
        acertos += 1
    else:
        acertos += 0

print(t)
print(resposta_dos_competidores)
print(acertos)
