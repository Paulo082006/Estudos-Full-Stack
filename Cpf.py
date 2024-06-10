def validar_cpf(cpf):
    # Ignora caracteres não decimais de um CPF
    cpf = ''.join(caractere for caractere in cpf if caractere.isdigit())
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito_1 = 11 - (soma % 11)
    if digito_1 > 9:
        digito_1 = 0
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito_2 = 11 - (soma % 11)
    if digito_2 > 9:
        digito_2 = 0
    # Verifica se os dígitos estão corretos
    if int(cpf[9]) != digito_1 or int(cpf[10]) != digito_2:
        return False
    return True

cpf = input("Digite o CPF a ser validado: ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
