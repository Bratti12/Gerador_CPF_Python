import os
os.system('cls')

def multiplicacao(*args):

    total = 1

    for numeros in args:
        total *= numeros

    return total

valor = multiplicacao(5 , 5)

print(valor)



def par_impar(x):

    if x % 2 == 0:
        return print('Este é um número par.')
    else:
        return print('Este é um número impar')
    

numero = par_impar(6)
