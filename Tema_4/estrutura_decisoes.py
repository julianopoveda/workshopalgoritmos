#um if simples
numero = 2

# numero % 2 efetua a divisao, porem o resultado retornado eh o resto da divisao e nao o quociente.
resto_divisao = numero % 2
if resto_divisao == 0:
    print("ola mundo")

somatorio = 1+1

#if-else: se entao, senao
nome_carro = "golf"

if nome_carro == "maverick":
    print("esse e V8 de verdade")
else:
    print("motor fraquinho")

nome_carro = "ipanema"

#previsao do tempo. Se entao, senao entao, senao

tempo = "chovendo"

if tempo == "chovendo":
    print("nao esquecer de pegar o guardachuvas")
elif tempo == "frio":
    print("tenho frio, vou colocar uma jaqueta")
elif tempo != "nublado":
    print("colocando oculos de sol")
else:
    print("quase esqueci da minha mochila")

# testes de numeros. Neste caso nao temos o bloco else que seria a execucao "Padrao" caso todos os testes falhem
if somatorio > 2:
    somatorio += + 2 #a notacao += e equivalente a somatorio = somatorio + 2
elif somatorio < 0:
    somatorio = 35
elif somatorio >= 1:
    somatorio = 15

somatorio = 0