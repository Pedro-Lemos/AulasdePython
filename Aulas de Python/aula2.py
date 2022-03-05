a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#print('Soma:', soma, 'Subtração:', subtracao)
resultado = ('Soma: {}. \nSubtração: {}.'
      ' \nMultiplicação: {}. '
      '\nDivisão: {}. '
      '\nResto: {}'.format(soma, subtracao, multiplicacao, divisao, resto))
print(resultado)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)