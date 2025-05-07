aluno = {'Nome': 'Pedro',
         'Email': 'pedro@senac.com',
         'Idade': 25,
         'Curso': 'Análise de Dados'}

print(aluno['Nome'])
print(aluno['Curso'])
print(aluno['Email'])
print(aluno['Idade'])

aluno['Email'] = 'pedro@senac.com.br'

print(aluno['Email'])

for chaves, valor in aluno.items():
    print(valor)
