
primeiro_numero = 0
segundo_numero = 1

print primeiro_numero
print segundo_numero 

numero_anterior = primeiro_numero
numero_atual = segundo_numero

imprimir_ate_numero = 10
numero_impresso = 3
while numero_impresso <= imprimir_ate_numero:
    proximo_numero = numero_atual + numero_anterior
    print proximo_numero    
    numero_anterior = numero_atual
    numero_atual = proximo_numero
    numero_impresso+= 1
