# Formatando valores com modificadores - Aula 5
# :s - Texto (strings)
# :d - Inteiros (int)
# :f - Ponto flutuante (float)
# :.(NÚMERO)f - Ponto flutuante com casas decimais
# :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, ou f)

# > - Esquerda
# < - Direita
# ^ - Centro

num1 = 123
num2 = 3
divisao = num1 / num2

print(divisao)
print("{}".format(divisao))
print("{:.2f}".format(divisao))
print(f"{divisao:.2f}")

# alinhamento de inteiro
print(f"{num1:0>10}")   # com dez dígitos alinhados à direita e zeros à esquerda
print(f"{num1:0<10}")   # com dez dígitos alinhados à esquerda e zeros à direita
print(f"{num1:0^10}")   # com dez dígitos alinhados ao centro e zeros à esquerda e à direita

# alinhamento como float
print(f"{num1:.2f}")
print(f"{num1:0>10.2f}")
print(f"{num1:0<10.2f}")
print(f"{num1:0^10.2f}")

# alinhamento de string
nome = "Alexandre Rodrigues"
nome_formatado = "{:*<50}".format(nome)
print(nome)
print(nome_formatado)
print(f"{nome:@<50}")

print(nome.lower())
print(nome.upper())
print(nome.title()) # campitalizado






