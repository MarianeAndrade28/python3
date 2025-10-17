# Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com os termos abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade; Acima de 40: Obesidade mórbida.


peso = float(input("Qual é o seu peso (Kg)?: "))
altura = float(input("Qual a sua altura (m)?: "))
imc = peso / (altura * altura)

print("="*30)
print(f"Seu IMC é de {imc:.1f}")
print("Sua condição é: ", end="")
if imc < 18.5:
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("PESO IDEAL")
elif 25 <= imc < 30:
    print("SOBREPESO")
elif 30 <= imc < 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MÓRBIDA")
