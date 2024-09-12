"""
Código para fazer a verificação do primerio dígito do CPF

CPF utilizado = 542.123.720-61

Primeiro passo é fazer a soma dos 9 dígitos e depois multiplicar numa contagem
regressiva começando de 10.
Exemplo:

CPF :           5   4   2   1   2   3   7   2   0
Multiplicação: 10   9   8   7   6   5   4   3   2
Resultado:     50  36  16   7  12  15  26   6   0

Após isso somar todos os valores de "Resultado"
Valor = 170
Depois multiplicar o resultado anterior por 10. 
170 * 10 = 1700
Depois, obter o resto da divisão da conta por 11
1700 % 11 = 6

Se o resto da divisão anterior for maior que 9:
        resultado é 0
o contrário disso:
        resultado é o valor da conta
    O primeiro digito do CPF é 6.
"""
import os
os.system('cls')
cpf = '542123720'
soma = (5*10) + (4*9) + (2*8) + (1*7) + (2*6) + (3*5) + (7*4) + (2*3) + (0*2)

multiplicao = soma * 10

resto_divisao = multiplicao % 11

if resto_divisao >= 10:  
    primeiro_digito = 0  
else:
    primeiro_digito = resto_divisao  

print(f'Primeiro dígito: {primeiro_digito}')

# Com o código acima obtivemos o primeiro dígito, para o segundo, a conta é exatamente a mesma, porém adicionarmos ele no final da conta
"""
CPF :           5   4   2   1   2   3   7   2   0   6
Multiplicação: 11  10   9   8   7   6   5   4   3   2
Resultado:     55  40  18   8  14  18  35   8   0  12

"""
cpf_2_digito = '5421237206'
soma_2 = (5*11) + (4*10) + (2*9) + (1*8) + (2*7) + (3*6) + (7*5) + (2*4) + (0*3) + (6*2)

multiplicao_2 = soma_2 * 10

resto_divisao_2 = multiplicao_2 % 11

if resto_divisao_2 >= 10:  
    segundo_digito = 0  
else:
    segundo_digito = resto_divisao_2  

print(f'Segundo dígito: {segundo_digito}')
