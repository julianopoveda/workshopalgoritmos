#-*- coding: utf-8 -*-
def PessoaAptaParcelamento(idade_pessoa, quantidade_parcelas) :
    quantidade_maxima_parcela_geral = 60
    quantidade_maxima_parcela_idoso = 36
    
    #primeiro efetua-se a verificação mais restritiva.
    if(idade_pessoa > 74 and quantidade_parcelas>quantidade_maxima_parcela_idoso):
        print ("Desculpe, porém não é possível fazer um parcelamento superior a %dx para pessoas na sua faixa etária" % quantidade_maxima_parcela_idoso)
        return False
    #Na segunda condição não é necessário verificar a idade, pois existe restrição somente para idosos.
    elif quantidade_parcelas>quantidade_maxima_parcela_geral:
        print ("Desculpe, porém não é possível fazer um parcelamento superior a %dx" % quantidade_maxima_parcela_geral)        
        return False
    else:
        return True

def ObterTaxaJuros(idade_pessoa):
    taxa_juros = 0

    #Essas variáveis servem para tornar o código mais legível e evitar muitos comentários de explicação
    faixa_45 = 45
    faixa_74 = 74
    faixa_75_mais = 75
    taxa_juros_ate_45_anos = 0.01
    taxa_juros_de_46_ate_74_anos = 0.02
    taxa_juros_a_partir_75_anos = 0.03
    
    #Aqui a variável de taxa_juros é iniciada. 
    #Não é interessante de realizar essa verificação dentro do laço, pois o valor da taxa não depende de nenhum componente do laço
    if(idade_pessoa <= faixa_45 ):
        taxa_juros = taxa_juros_ate_45_anos
    elif(idade_pessoa>faixa_45 and idade_pessoa <=faixa_74):
        taxa_juros = taxa_juros_de_46_ate_74_anos
    else:
        taxa_juros = taxa_juros_a_partir_75_anos
    
    return taxa_juros

def CorrigirValorParcela(valor_parcela, taxa_juros, mes_corrente):
    adendo_de_parcela = mes_corrente / 2
    valor_parcela_corrigido = valor_parcela * ( 1 + taxa_juros ) + adendo_de_parcela
    return valor_parcela_corrigido

def CalcularEmprestimo(valor_emprestimo, quantidade_parcelas, idade_pessoa):    
    valor_parcela = valor_emprestimo/quantidade_parcelas
    taxa_juros = ObterTaxaJuros(idade_pessoa)
    
    mes_corrente = 1    
    valor_total = 0

    while(mes_corrente <= quantidade_parcelas):        
        valor_total = valor_total + CorrigirValorParcela(valor_parcela, taxa_juros, mes_corrente)
        mes_corrente += 1 #esta expressão equivale a: mes_corrente = mes_corrente + 1
    
    return valor_total

def GerarRelatorio(nome_cliente, valor_emprestimo, quantidade_parcelas, valor_ultima_parcela_corrigida, valor_total_emprestimo):
    #o caracter \n simboliza quebra de linha, desta forma não é preciso colocar um print para cada linha impressa
    print("Sr(a): %s \nValor de empréstimo solicitado: %.2f \nQuantidade de Parcelas: %d \nValor da última parcela: %.2f \nValor Total do Empréstimo:%.2f" % (nome_cliente, valor_emprestimo, quantidade_parcelas, valor_ultima_parcela_corrigida, valor_total_emprestimo))


#Aqui começa a rodar o programa
valor_emprestimo = 5000.00
quantidade_parcelas = 60
idade_pessoa = 23
nome_cliente ="Fulano de Tal"

if PessoaAptaParcelamento(idade_pessoa, quantidade_parcelas):
    valor_total_emprestimo = CalcularEmprestimo(valor_emprestimo, quantidade_parcelas, idade_pessoa)
    
    #Para obter a última parcela, basta chamar mais uma vez o método CorrigirValorParcela, informando os valores
    #Aqui resolvi passar chamadas de outros métodos e contas matemáticas como parâmetro para mostrar que não é somente com valores estáticos que posso passar valores para um método
    valor_ultima_parcela_corrigida = CorrigirValorParcela(valor_emprestimo / quantidade_parcelas, ObterTaxaJuros(idade_pessoa), quantidade_parcelas)

    GerarRelatorio(nome_cliente, valor_emprestimo, quantidade_parcelas, valor_ultima_parcela_corrigida, valor_total_emprestimo)
else:
    print("Lamentamos não poder realizar seu empréstimo")