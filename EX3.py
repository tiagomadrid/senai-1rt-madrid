salario = float(input("Qual seu salario?: "))

aumento = salario + (salario * 0.10)
aumento2 = salario + (salario * 0.15)

if salario >= 8250.00:
    print("Seu novo salario e de R$: ",aumento)

else:
    print("Seu novo salario e de R$: ",aumento2)
