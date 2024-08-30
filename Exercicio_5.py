
def inverter_string(s):
    
    resultado = ''

    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado


entrada = input("Digite a string que deseja inverter: ")


print("String invertida:", inverter_string(entrada))