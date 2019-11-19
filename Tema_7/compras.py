#-*- coding: utf-8 -*- #com isso posso usar acentos

def Calcular_Valor_Total_Conta (valor_original, taxa_juros, desconto_a_ser_aplicado):
    valor_corrigido = valor_original * (1 + taxa_juros)
    valor_com_desconto = valor_corrigido * (1 - desconto_a_ser_aplicado)
    return valor_com_desconto

def Imprimir_Fatura (valor_total_compra):
    print "O valor total da sua compra é: R$ %.2f" % valor_total_compra


#Aqui seria o programa princial, nos mesmos moldes que estudamos até agora
calca = 100
tenis = 300
camiseta = 40
meias = 10
roupa_intima = 20

valor_total = calca * 3
valor_total += (camiseta * 5) #quando colocamos parênteses, assim como na matemática da escola, estamos dizendo para o Python primeiro resolver o que está dentro dele e depois o resto
valor_total += tenis
valor_total += meias * 7 
valor_total += roupa_intima * 7

taxa_parcelamento = 0.025
desconto = 0.13

#A troca dos nomes das variáveis informadas no lugar dos parâmetros é proposital, justamente para mostrar que o nome da variável não importa fora do método
valor_total_compra_com_desconto = Calcular_Valor_Total_Conta(valor_total, taxa_parcelamento, 0.13)

#O if é somente para dar um charme :D
if valor_total_compra_com_desconto > 0:
    Imprimir_Fatura(valor_total_compra_com_desconto)
else:
    print "Parabéns sua fatura não possui valor de cobrança"