def cadasrar_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = float(input('Informe o valor da venda: '))

        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lista_vendedor_vendas.append(pessoa)


def calcula_total_media():
    tot = 0
    for pessoa in lista_vendedor_vendas:
        tot += pessoa['Valor']
    med = tot/len(lista_vendedor_vendas)

    return tot, med


lista_vendedor_vendas = []

qtd = int(input('Quantas pessoas? '))
cadasrar_pessoa(qtd)

print(lista_vendedor_vendas)

total, media = calcula_total_media()

print(f'Valores Total de vendas R${total:.2f} e média de vendas R${media:.2f}')
