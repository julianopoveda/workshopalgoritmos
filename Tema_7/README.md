# 7. Métodos
Vamos começar essa aula com a seguinte pergunta:

> Quantas vezes você já teve de fazer uma tarefa repetitiva?

Em algoritmos, blocos de código também se repetem. Agora imagine ter que ficar repetindo o seguinte trecho de código em diversos pontos do algoritmo

```Python
    ...
    valor_corrigido = valor_original * (1 + taxa_juros)
    valor_com_desconto = valor_corrigido (1 - desconto_a_ser_aplicado)

    print "O valor total da sua compra é: R$" str(valor_com_desconto)    
    ...
```
Pior que replicar este código é dar manutenção com ele espalhado em todo o sistema.

Para facilitar este tipo de chamada, criam-se métodos. Métodos nada mais são que pequenos trechos de código(pelo menos deveria :)) encapsuldos dentro de um bloco(lembrem do bloco do if) e possuem um nome para identificá-lo. 

O bloco mostrado anteriormente ficaria assim se fosse transformado em método

```Python
def Valor_Total_Compra (valor_original, taxa_juros, desconto_a_ser_aplicado):
    valor_corrigido = valor_original * (1 + taxa_juros)
    valor_com_desconto = valor_corrigido (1 - desconto_a_ser_aplicado)

    print "O valor total da sua compra é: R$" str(valor_com_desconto)
```

Você deve estar se perguntando 
> Por que **valor_original, taxa_juros e desconto_a_ser_aplicado** estão do lado do nome do método?

Pois bem, quando os valores ou [variáveis(conforme aprendemos na aula 3)](Tema_3/README.md) estão ao lado do nome do método elas são conhecidas como parâmetros. Os parâmetros existem para que possamos informar valores que serão utilizados pelo método, porém que não são de conhecimento e responsabilidade deste.

> E o que significa esse `def`?

O def é justamente quem diz para o Python que o bloco nominado é um método. Lembre o computador não é inteligente para saber dessas coisas, ele somente faz o que dizem para ele. Então, os inteligentes somos nós :)

### 7.1 Métodos retornam valores?
Sim, métodos também podem retornar valores. Imagine o exemplo do método acima, porém este método é quebrado em *Calcular_Valor_Total_Conta* e *Imprimir_Fatura*. O resultado seria mais ou menos assim:


``` Python
def Calcular_Valor_Total_Conta (valor_original, taxa_juros, desconto_a_ser_aplicado):
    valor_corrigido = valor_original * (1 + taxa_juros)
    valor_com_desconto = valor_corrigido (1 - desconto_a_ser_aplicado)
    return valor_com_desconto

def Imprimir_Fatura (valor_total_compra):
    print "O valor total da sua compra é: R$" str(valor_total_compra)

#Aqui seria o programa princial, nos mesmos moldes que estudamos até agora

valor_total_compra_com_desconto = Calcular_Valor_Total_Conta(1000, 0.025, 0.13)

#O if é somente para dar um charme :D
if valor_total_compra_com_desconto > 0:
    Imprimir_Fatura(valor_total_compra_com_desconto)
else:
    print "Parabéns sua fatura não possui valor de cobrança
```
*Sugestão*: Experimente pegar o programa das aulas 3 e 4 e separar os blocos em métodos e tente utilizar algum destes métodos mais de uma vez

---
Próximo assunto: [Desafio](../Tema_8/README.md)