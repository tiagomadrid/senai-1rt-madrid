viagem = float(input("Qual a distancia da viagem?: "))
passagem = 0.50 * viagem
passagem2 = 0.45 * viagem

if viagem >= 200:
    print("O preco da viagem e de: ",passagem2)

else:
    print("O preco da viagem e de: ",passagem)
