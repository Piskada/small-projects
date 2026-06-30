# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite a temperatura em °C:"))
tp_temperatura = input("Digite a temperatura que deseja converter (K/F): ").upper()

match tp_temperatura:
    case "K":
        temperatura_convertida = temperatura + 273
    case "F":
        temperatura_convertida = temperatura *9/5 + 32

print(f"A temperatura de {temperatura}°C convertida para {tp_temperatura} é: {temperatura_convertida:.2f}{tp_temperatura}")