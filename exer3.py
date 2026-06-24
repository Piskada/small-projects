while True:
    try: 
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        soma = n1 + n2
        print(f'A soma de {n1} e {n2}\né igual a {soma}.')
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

        