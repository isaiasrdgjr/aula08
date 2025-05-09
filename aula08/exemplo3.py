def cadasrar_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = float(input('Informe o valor da venda: '))

        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lista_vendedor_vendas.append(pessoa)


lista_vendedor_vendas = []

qtd = int(input('Quantas pessoas? '))
cadasrar_pessoa(qtd)

print(lista_vendedor_vendas)
