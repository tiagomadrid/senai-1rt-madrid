numero = float(input("Insira um numero: "))
numero2 = float(input("Insira outro numero: "))
operacao = input("Escolha um operador como: +, - , * e /: ")

if  operacao == "+":
    resultado = numero + numero2
elif operacao == "-":
    resultado = numero - numero2
elif operacao == "*":
    resultado = numero * numero2
elif operacao == "/":
    resultado = numero / numero2

else:
    print("Operacao invalida")

print("O resultado e: ",resultado)