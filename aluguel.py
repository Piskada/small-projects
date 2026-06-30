#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km_percorridos = float(input("Digite a quantidade de km percorridos: "))

print('=' * 50)
valor_total = (dias * 60) + (km_percorridos * 0.15)
print(f"O valor total a ser pago pelo aluguel do carro é: R${valor_total:.2f}")