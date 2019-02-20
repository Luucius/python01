nome = str(input('Seu Nome: '))
idade = int(input("Sua Idade: "))

if idade >= 18:
    print(nome + ', pode entrar.')
elif idade < 11:
    print(nome + ', você é uma criança.')
else:
    print(nome + ', você é menor de idade.')