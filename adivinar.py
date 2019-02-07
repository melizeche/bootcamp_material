from random import randint

numero = randint(0,100)

adivino = False
while(adivino==False):
    num2 = int(input("Ingresa un numero: "))
    if num2==numero:
        adivino=True
        print("BIEN!!! ADIVINASTE!!!")
    else:
        print("Proba de nuevo")

# Ej. Crear un juego de adivinanzas que el usuario trate de adivinar un numero
# y que te de pistas si el numero ingresado es menor o mayor al numero a adivinar