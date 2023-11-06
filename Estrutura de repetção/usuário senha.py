usuário=input('Usuário==> ')
senha=(input('Senha==> '))
while senha==usuário:
    print('ERRO')
    usuário=input('Usuário==> ')
    senha=int(input('Senha==> '))