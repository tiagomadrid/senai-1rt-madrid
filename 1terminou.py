velocidade = float(input("Qual a velocidade do carro?: "))
velocidade2 = velocidade - 80

if velocidade >=80:
    reais = velocidade2 * 7
    print(f"Voce foi multado, estava a {velocidade} km e o preco e {reais:.2f} reais")