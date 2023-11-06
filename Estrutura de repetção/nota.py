# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota=float(input("informe um numero de 0 a 10: ")) #Pedindo a nota
while (nota>10) or (nota<0): #enquanto nota for maior que 10 ou menor que 0 pede denovo
	nota=float(input("informe um numero de 0 a 10: "))