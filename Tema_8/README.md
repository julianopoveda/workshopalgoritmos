# 8. Desafio

Foi uma caminhada ardua para chegarmos até aqui!

Agradeço a todos que acompanharam este workshop até o fim. Qualquer critica ou sugestão é bem vinda :D

Agora para fecharmos o workshop, que tal um desafio para colocarmos em prática tudo que foi aprendido?

## 8.1 Enunciado

Você deve montar uma espécie de cálculo de empréstimo para um grande banco. Como o banco não é tão bonzinho assim para emprestar dinheiro sem algumas restrições, vamos a elas:

- O empréstimo pode ser parcelado no máximo em 60x
- Pessoas com mais de 75 anos podem parcelar o empréstimo no máximo em 36x
    - Se o valor for superior a 36x deve ser emitida uma mensagem: "Desculpe, porém não é possível fazer um parcelamento superior a 36x para pessoas na sua faixa etária"(ou uma mensagem parecida, seja criativo :))
- O valor original do empréstimo deve ser dividido em parcelas iguais e depois essas parcelas devem ser corrigidas conforme as regras abaixo:
    - A cada mês deve ser adicionado **n** reais no valor parcela, sendo o n o número da parcela divido por dois. Ex: o número da parcela é 24, então n será 12
    - A taxa de juros aumenta conforme a idade:
        - até os 45 anos a taxa é 1%
        - de 46 a 74 anos a taxa é 2%
        - a partir de 75 anos a taxa é 3%

Exemplo da fórmula do calculo da parcela

```Python
valor_parcela_corrigido = valor_parcela * ( 1 + taxa_juros) + n
```

### Relatório 8.1.1
Ao final do cálculo deve ser impresso um relatório para o cliente informando:

- O nome do cliente
- O Valor solicitado do empréstimo
- Em quantas vezes o empréstimo foi feito
- O valor da última parcela a ser paga
- O valor total a ser pago

## 8.2 Dicas

1. Consulte o material já estudado para relembrar como se escrevem: if, while e métodos
2. Tente evitar fazer os cálculos se não for possível realizar o empréstimo (olhe restrições de idade e parcelamento ;) )
3. Tente agrupar etapas do programa em métodos (olha a [aula 7](../Tema_7/README.md))
4. Não tenha vergonha de pedir ajuda