def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False
def main():
    while True:
        cpf = input("Digite o CPF a ser validado (somente números): ")
        if validar_cpf(cpf):
            print("CPF válido.")
        else:
            print("CPF inválido.")


if __name__ == "__main__":
    main()

