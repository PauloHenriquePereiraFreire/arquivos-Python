num=int(input('Digite um número de 1 a 50: '))
while num < 1 or num > 50:
    num=int(input('Número fora do intervalo! Digite novamente: '))
print('Número aceito!')