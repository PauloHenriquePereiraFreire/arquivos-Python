print('Digite o valor que está à esquerda da vírgula:')
grau_inteiro= int(input())
print('Digite o valor que está à direita da vírgula iniciando com 0.:')
decimal= float(input())
minuto_preliminar = decimal * 60
minuto = int(minuto_preliminar)
segundo = (minuto_preliminar - int(minuto_preliminar)) * 60
print('O valor do grau é:' ,grau_inteiro)
print('O valor do minuto é:' ,minuto)
print('O valor do segundo é: %.3f' %segundo)