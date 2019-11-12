# 2. Variáveis e operações matemáticas
Como já mencionado em "[O que são algoritmos?](../Tema_1/README.md)", os algoritmos provem de um método metemático. Por tratar-se de uma abstração matemática, os algoritmos também valem-se de outros recursos matemáticos, tais como as variáveis e as operações matemáticas.

[Neste link temos o mesmo código que encontra-se no projeto](https://hub.gke.mybinder.org/user/ipython-ipython-in-depth-s0xe1c6b/notebooks/binder/Tema_3.ipynb)

## 2.1. Variáveis
Variáveis, assim como o nome já diz, são entidades que variam seu valor. 
Variáveis podem ser atribuídas com constantes, por outras variáveis ou por uma combinação de constantes e outras variáveis, através de operações matemáticas
> Isso significa que podemos atribuir qualquer valor a uma variável?

A resposta é sim e não. 
Diversas linguagens requerem que o tipo da variável seja definida e uma vez que este tipo é definido para a variável, ele não pode mais ser alterado.

Exemplos de linguagens que necessitam de declaração de tipo nas suas variáveis:

    - C#
    - Java
    - Go

Já outras linguagens não exigem esta tipagem, como é o caso do Javascript, que uma hora pode ser um número e na outra uma palavra.

No caso de Python a linguagem não exige que o programador diga explicitamente qual é o tipo da variável, porém uma vez atribuido o valor, o próprio Python preocupa-se em determinar o tipo e impedir a mudança de tipo daquela variável.

Os tipos mais conhecidos são

| Tipo | Breve explicação | 
|------|------------------|
| int  | Representam o conjunto dos inteiros|
| float| Números de ponto flutuante, muito utilizado em notação cientifica|
| char | Representa um caractére e somente um caractére|
| string| Um conjunto de caractéres, normalmente utilizados para formar uma palavra|
| bool| Simboliza o resultado de um teste, sendo True para *verdadeiro* e False para *falso*|

## 2.2. Operações matemáticas
Toda linguagem de programação possui pelo menos as 4 operações básicas: soma, subtração, multiplicação e divisão. No entanto, operações mais complexas como potenciação e integrais podem ser encontradas na vasta maioria das linguagens através de bibliotecas prontas (bibliotecas são pequenos trechos de códigos que podem ser reaproveitados.)


### Experimente trocar a segunda atribuição da variável largura para o valor "jujuba" ou "10" e veja o erro que acontece

Próximo assunto: [Estruturas de decisões](../Tema_4/README.md)