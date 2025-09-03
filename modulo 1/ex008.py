# Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

from time import sleep
print("============ CONVERSOR DE MEDIDAS ============")
metros = float(input("Qual o valor em metros?: "))
print("="*45)
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000


print("Convertendo...")
sleep(2)
print(f"""O valor em metros é: {metros}m
      Convertido em quilômetros é: {km}km
      Convertido em hectômetro é: {hm}hm
      Convertido em decâmetro é: {dam}dam
      Convertido em decímetro é: {dm}dm
      Convertido em centímetro é: {cm}cm
      Convertido em milímetro é: {mm}mm""")
print("="*45)
