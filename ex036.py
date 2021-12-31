'''decide se o emprestimo será liberado conforme o valor da prestação,
que não deve passar de 30% do salário '''

print('---------EMPRESTIMO BANCARIO------------')
casa=float(input('Qual o valor da casa? '))
salario=float(input('Qual o valor do seu salário? '))
anos=int(input('Em quantos anos você pretende pagar a casa? '))
print('-----------------------------------------')
prest= casa/(12*anos)
#Teste condicional
if prest>(0.3*salario):
    print('Desculpe senhor,mas não podemos liberar o emprestimo no momento.')
else:
    print('O valor da sua parcela é de R$ {:.2f} '.format(prest))
print('-----OBRIGADO POR USAR O PROGRAMA!--------------')