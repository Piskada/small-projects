# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")
print(f"Nome em maiúsculas: {nome.upper()} \n Nome em minúsculas: {nome.lower()}")
print(f"Quantidade de letras (sem espaços): {len(nome.replace(' ', ''))}")
print(f"Seu nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.")
