# 6. Laços

Com o conhecimento adquirido até aqui, como resolveríamos a seguinte questão:

> Conhecendo a [sequência de Fibonacci](https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci), necessito calcular e imprimir até a terceira posição.

Vamos lá:
Primeiro ponto, para quem não conhece a fórmula para calcular a sequência é a seguinte

```Proximo_numero = Numero_Atual + Numero_Anterior```

O primeiro número da sequência é zero e o segundo número da sequência é Um. A partir deles podemos seguir calculando a sequencia utilizando a fórmula já mencionada.

---
Antes de seguirmos, dá uma conferida nesse vídeo se ainda não conheces a sequência de fibonacci[![Donald no país da matemágica](https://livrandante.com.br/wp-content/uploads/2017/01/Donald-no-Pa%C3%ADs-da-Matem%C3%A1gica.jpg)](https://youtu.be/wbftu093Yqk?t=441)

--- 
Voltando para problemática o código para resolver está questão parece bem simples

```Python
primeiro_numero = 0
segundo_numero = 1

print primeiro_numero
print segundo_numero 

proximo_numero = primeiro_numero + segundo_numero
print proximo_numero
```

Agora o que acontece se pedirmos para imprimir até o quarto número da sequência?

```Python
primeiro_numero = 0
segundo_numero = 1

print primeiro_numero
print segundo_numero 

proximo_numero = primeiro_numero + segundo_numero
print proximo_numero

numero_anterior = segundo_numero
numero_atual = proximo_numero

proximo_numero = numero_atual + numero_anterior
print proximo_numero
```

hmm, está ficando muito repetitivo.
Agora se eu quiser até o décimo número ou até um número arbitrário? Nota-se que não é possível continuar com esse copia e cola o tempo todo.

> Então como evitar repetir esse trecho de código indefinidamente?

Para este tipo de situação temos as estruturas de laço `while` e `for`

Nesta aula vou ater-me somente no while por possuir uma estrutura mais simples e por consequencia mais fácil de entender.

## 4.1 While
Se for buscada a tradução da palavra ela seria traduzida para **Enquanto**. O While da programação é exatamente isso, enquanto a condição for satisfeita o trecho de código dentro do while será executado

```Python
while condicao_verdadeira: 
    ...
    print proximo_numero
    ...
```

> Mas como o Python sabe onde fica o bloco de código que o while deve executar?

O Python trabalha com escopo por identação. Isso significa que tudo que estiver com um tab a mais que a declaração do while será considerado pertencente ao bloco do while.

Note que a condição sempre será testada antes de executar o bloco, isso significa que, se o teste do while falhar de primeira, o bloco de código não será executado.

Dá uma conferida como ficaria a versão do fibonacci aqui. Mas só depois de tentar solucionar ;)


## 4.2 For
O For geralmente tem aplicação para percorrer listas com inicio e fim bem definidos.
Já o while é sempre indicado para laços que não se sabe quando ele deve parar, somente qual condição deve ser atendida para ele parar.

---
Próximo assunto: [Métodos](../Tema_7/README.md)