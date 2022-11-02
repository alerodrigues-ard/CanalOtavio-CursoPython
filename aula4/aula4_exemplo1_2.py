# Operadores Lógicos - Aula 4

# and, or e not
# in e not in

# in e not in

nome = "Alexandre"
letra = 'a'
trecho = "xan"

if letra in nome:
    print(f"O nome {nome} tem a letra {letra}")
else:
    print(f"O nome {nome} não tem a letra {letra}")

if trecho in nome:
    print(f"O nome {nome} tem a trecho {trecho}")
else:
    print(f"O nome {nome} não tem o trecho {trecho}")

if trecho not in nome:
    print(f"O nome {nome} não tem o trecho {trecho}")    
else:
    print(f"O nome {nome} tem a trecho {trecho}")


