'''Faça um programa que apresente se o número que o usuário
digitou é divisível por 3 e por 5 ao mesmo tempo.'''
print("Digite um número: ")
num = int(input())  
    
if num%3==0 and num%5==0:
    print('O número é divisivel por 3 e 5')
else:
    print('O número é não é divisivel por 3 e 5')
