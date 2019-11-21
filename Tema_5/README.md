# Trabalhando com Strings

Até o momento temos visto "frases entre aspas" como esta nos temas anteriores. O que exatamente é essa notação?
Strings!

[String](https://docs.python.org/2/library/string.html) é o tipo que representa textos quando estamos programando. Elas são úteis quando queremos emitir mensagens para o usuário(pessoa que esta interagindo com o programa).

Strings costumam ser o tipo mais utilizado para realizar uma interface de comunicação com o usuário ([entradas e saídas](../Tema_8/README.md)) e para a maioria dos dados salvos em bancos de dados(lugares onde a informação é salva de maneira estruturada, imaginem algo parecido com um planilhão excel com várias abas, só que mais difícil :) )

Strings são poderosas principalmente por aceitarem qualquer tipo de informação, desde que seja possível escrevê-la como texto. 
Ex: Podemos representar um número como:
- 10
- 10.00
- R$ 10.00
- U$ 10.00

Todos os casos podem ser representados de forma textual, porém somente os dois primeiros podem ser descritos para os tipos inteiro e decimal.

Em todas linguagens de programação podemos concatenar strings com outros tipos, inclusive com strings utilizando o sinal de "+" (caso do Python e de muitas outras linguagens).
Qualquer linguagem que possua tipos possui métodos especiais chamados **ToString** para converter qualquer tipo em string e métodos de **Parsing** para converter string em um tipo especifico.

No exemplo .py desta aula (link online aqui :D ) mostram diversos tipos de operações com string. Confere lá.

> Antes de continuarmos, você deve ter notado que as strings e comentários apresentados até agora nos códigos não possuem acentos. Esse comportamento se deve ao fato de por padrão o Python só apresentar caractéres [ANSI](https://pt.wikipedia.org/wiki/ASCII), para resolvermos este problema declaramos a linha a seguir como a primeira linha do arquivo de código 
```Python
#-*- coding: utf-8 -*- 
```
> Esta linha informa para o interpretador do Python como ele deve "desenhar" o código que representa aquela letra/número/símbolo na tela.

---
Próximo assunto: [Laços](../Tema_6/README.md)