# Strings
print("Teste de aspas \"  \' - Terminou")
print('Teste de aspas \"  \' - Terminou')

# Operadores
print(5/2)
print(5//2)

# Variáveis
# Tipagem dinâmica
# Convenções: letras minúsculas
#             palavras deparadas por _
nome = "Alexandre"
idade = 53
print(nome)

# Método format
print("Meu nome é {}".format(nome))
print("Meu nome é {nm} e tenho {id} anos".format(nm=nome, id=idade))    # com parâmetros nomeados
print("Meu nome é {0} e tenho {1} anos mesmo".format(nome, idade))      # com parâmetros posicionais

# Interpolação
print(f"Meu nome é {nome} e eu tenho {idade} anos")

# Tipos de dados
print(f"O tipo da variável nome é {type(nome)}")
print(f"O tipo da variável idade é {type(idade)}")

valor_texto = '9.3'
print(f"Como texto \"{valor_texto}\"")
print(f"Como float {float(valor_texto)}")
print(f"Como int {int(float(valor_texto))}")

