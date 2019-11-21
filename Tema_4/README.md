# 4. Estrutura de decisões

Até o momento temos visto uma progressão muito linear, muito certeira de como as instruções devem ser executadas. Porém, a realidade não é linear. 
Pense na seguinte afirmativas:
1. Se chover, devo levo o guardachuvas, caso contrário irei me molhar
2. Esta frio, logo devo colocar um casaco

As mesmas afirmativas poderiam ser invertidas:

3. O tempo dia esta ensolarado, logo posso deixar o guardachuvas em casa pois não irei me molhar
4. Esta quente, logo posso tirar o casaco.

Nota-se claramente uma condição para os casos de levar um guardachuvas ou colocar um casaco. No desenvolvimento de algoritmos ocorre exatamente o mesmo. Existem trechos de instruções (para facilitar vou começar a chamar de código) que devem se executados quando uma ou mais condições forem satisfeitas, caso contrário não devem ser executados. Também existe o caso onde um código deve ser executado caso a condição ou as condições não sejam satisfeitas ou em termos de máquina se for verdadeira e outro código deve ser executado caso a condição ou condições não sejam atendidas.

**E como se representa essa estrutura de decisão?**

Através do bloco if e os operadores booleanos.

## 4.1 O que são operadores booleanos?
Operadores booleanos nada mais são do que operações matemáticas sobre valores booleanos.

> Iiii, agora complicou.

### Calma!
Valores booleanos, são os valores **Verdadeiro** e **Falso**, ou **True** e **False** no python. 
Lembra daquelas questõs de *Assinale V para as afirmativas verdadeiras e F para as falsas, justificando as falsas*? Então, essas questões são uma forma de teste booleano, a diferença é que neste caso somente quando a alternativa for **falsa** devemos executar o código específico, neste caso a justificativa.

Já as operações booleanas são representadas pelos seguintes operadores, que servem para juntar 1 ou mais testes booleanos

| Operador | Descrição |
|----------|-----------|
| ==       | Representa igualdade. Não confundir com o = simples que é o de atribuição |
| !=       | Representa diferença, ou seja se valor1 é diferente de valor2, o teste é verdadeiro |
| >        | Se valor1 é maior valor2, o teste é verdadeiro |
| <        | Se valor1 é menor valor2, o teste é verdadeiro |
| >=       | Se valor1 é maior ou igual valor2, o teste é verdadeiro |
| <=       | Se valor1 é menor ou igual valor2, o teste é verdadeiro |
| &&       | Se valor1 e valor2 são verdadeiros, o teste é verdadeiro|
| \|\|     | Se o valor1 ou o valor2 ou ambos forem verdadeiros, o teste é verdadeiro|
| !        | Inverte o resultado do teste, ou seja, se o teste for verdadeiro ele retorna false e vice-versa|

## 4.2 O Bloco if
Após entender o que são os operadores e valores booleanos, é interessante saber onde eles serão usados majoritariamente. O bloco if serve para encapsular um código que só deve ser executado se o teste contido ao lado do if for verdadeiro

Exemplo de um bloco if

```[Python]
numero = 2

# numero % 2 efetua a divisao, porém o resultado retornado é o resto da divisão e não o quociente.
if numero % 2 == 0:
    print("ola mundo")

somatorio = 1+1
```
O bloco acima só irá imprimir *"olá mundo"* se o número informado for par

O próximo bloco imprime *"esse é V8 de verdade"* caso o nome do carro for maverick, caso contrário irá imprimir *"motor fraquinho"*

```[Python]
nome_carro = "golf"

if nome_carro == "maverick":
    print("esse e V8 de verdade")
else:
    print("motor fraquinho")

nome_carro = "ipanema"
```

por fim temos o encadeamento de testes, pois podemos ter a seguinte situação:

1. Se está chovendo, devo levar o guardachuvas
2. Senão se está frio, devo colocar uma jaqueta
3. Senão se não esta nublado, devo pegar meu óculos de sol
4. Senão levo somente a mochila

```Python
tempo = "chovendo"

if tempo == "chovendo":
    print("nao esquecer de pegar o guardachuvas")
elif tempo == "frio":
    print("tenho frio, vou colocar uma jaqueta")
elif tempo != "nublado":
    print("colocando oculos de sol")
else:
    print("quase esqueci da minha mochila")

nome_carro = "ipanema"
```

[No arquivo de exemplo](https://notebooks.gesis.org/binder/jupyter/user/ipython-ipython-in-depth-upfbnlc1/notebooks/binder/estrutura%20de%20decisoes.ipynb) temos esses es outros exemplos de fluxo. Experimente trocar os valores das variáveis e ver o que acontece

---
Próximo assunto: [Trabalhando com Strings](../Tema_5/README.md)