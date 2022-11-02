# Entrada de dadows - Aula3

nome = input("Qual o seu nome? ")
idade = input(f"Qual a sua idade, {nome}? ")

ano_nascimento = 2022 - int(idade)

print(f"O seu nome é {nome} e você tem {idade} anos (você nasceu em {ano_nascimento - 1} ou {ano_nascimento})")
