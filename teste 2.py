try:
    n1 = int(input('pense em um número e depois digite ele aqui'))
    n2 = int(input('pense em outro e escreva aqui'))
    soma= n1+n2
    print('A soma dos números é igual',soma)

except ValueError:
    raise ValueError("mensagem")
