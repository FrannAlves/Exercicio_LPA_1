print('Bem vindo a loja Francielle Alves Sousa')
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Digite a quantidade: '))
sem_desconto = valor_produto * qtd_produto#valor total sem o desconto
if qtd_produto <= 4 :
    valor_final = valor_produto
elif qtd_produto >= 5 and qtd_produto <= 19 :#comprando entre 5 e 19 produtos o desconto será 3%
    percentual = 3
    valor_desconto = valor_produto - valor_produto * 0.03
    valor_final = valor_desconto * qtd_produto#valor total com o desconto de 3%
elif qtd_produto >= 20 and qtd_produto <= 99 :#comprando entre 20 e 99 produtos 

    percentual = 6
    valor_desconto = valor_produto - valor_produto * 0.06
    valor_final = valor_desconto * qtd_produto#valor total com desconto de 6%
else:#comprando mais de 100 produtos o desconto será 10%
    percentual = 10
    valor_desconto = valor_produto - valor_produto * 0.10
    valor_final = valor_desconto * qtd_produto#valor total com desconto de 10%
print('o valor sem desconto foi: R$ {:.2f}.'.format(sem_desconto))
print('O valor com desconto foi: R$ {:.2f} ({} % desconto)'.format(valor_final, percentual))


