# calculo do IMC

peso = float(input ('Qual é o seu peso?'))
altura = float(input ('Qual é a sua altura?'))

calculoimc = peso / altura**2

print (f'Seu IMC é {round (calculoimc, 2)}')


# lista de inteiros

inteiros = []
while len (inteiros) < 5:
    inserir_numero = int(input('Insira um número: '))
    inteiros.append(inserir_numero)
    
print (inteiros)


#lista de nomes

nome = []
inserir_nome = input('Insira seu nome completo, separado por vírgula: ')

nome.append(inserir_nome)

nome = inserir_nome.split(',')

print (nome)