# or i in range(1, 11):
#    print(f"Este é i: {i}")
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=', ')
print('Fim')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for a in aprovados:
    print(a)
for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1}) {nome}')

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('poxa vida porque nao embaralhou'):
    print(letra)

for i in range(1, 51):
    print(f"googobie {i}")
