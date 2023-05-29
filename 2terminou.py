nota = float(input("Insira sua nota na competicao: "))

if nota <= 50:
    print("Parabens, voce ganhou o certificado de participacao.")

elif  nota <= 60:
    print("Parabens, voce ganhou o certificado de mencao honrosa.")

elif nota <=70:
    print("Parabens, voce ganhou a medalha de bronze")

elif nota <=90:
    print("Parabens, voce ganhou a medalha de prata")

elif nota > 90:
    print("Parabens, voce ganhou a medalha de ouro")
