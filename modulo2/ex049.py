# Desafio 049: Refaça o "Desafio 009", mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input("Digite um número para ver sua tabuada: "))
print(f"==== TABUADA DO {tabuada} ====")
for c in range(1, 11):
    print("{} x {:2} = {:2}".format(tabuada, c, tabuada*c))
