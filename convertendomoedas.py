carteira = float(input("Digite o valor que você tem na carteira R$"))
moeda = input("Digite a moeda que você quer converter (USD ou EUR): ").upper()

match moeda:
    case 'USD':
        valor_convertido = carteira / 5.20
    case 'EUR':
        valor_convertido = carteira / 5.92

print(f'O valor convertido em {moeda} é de {valor_convertido:.2f}')