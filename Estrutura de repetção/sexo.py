while True:
    sexo=input('Qual o seu sexo?(F/M) ').strip()
    if 'M' not in sexo and 'F' not in sexo:
        print('Digite novamente...')
    else:
        nome=input('Qual o seu nome? ')
        if nome == '':
            print('Nome invalido')
        else:
            break