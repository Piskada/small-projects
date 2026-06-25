largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area:.2f}m² e a quantidade de tinta necessária para pintá-la é de {tinta:.2f}L')