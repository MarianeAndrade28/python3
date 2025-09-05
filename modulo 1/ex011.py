# Desafio 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro pinta uma área de 2m².

largura = float(input("Qual a largura da parede?: "))
altura = float(input("Qual a altura da parede?: "))
area = largura * altura
tinta = area / 2

print(f"As dimensões da parede são {largura:.2f}x{altura:.2f} e sua área é de {area:.2f}m²")
print(f"Para pintar essa parede, precisaremos de {tinta:.2f}l de tinta")
