n = 0 
for i in range(1,3):
    n += float(input())
média = n/i
if média < 5:
    print('REPROVADO')
elif média <= 6.9:
    print('RECUPERAÇÃO')
elif média >= 7:
    print('APROVADO')


