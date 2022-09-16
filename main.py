# Implemente um programa capaz de solicitar ao usuário suas notas da AV1 e da AV2. O programa deve imprimir qua é a sua média. 

print ('Vamos calcular a média das suas notas da AV1 e da AV2? ')

nome = input('Qual é o seu nome? \n')
av1 = input('Digite a nota da AV1: \n')
av2 = input('Digite a nota da AV2: \n')

media = ((int(av1) + int(av2))/2)
print (nome,', você teve média igual a:', media) 