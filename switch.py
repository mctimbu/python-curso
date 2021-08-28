def get_dia_semana(dia):
    dias = {
        1: 'Fim de semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Fim de semana',
    }
    return dias.get(dia, "Dia invalido a?mi?gao?")


if __name__ == '__main__':
    for dia in range(12):
        print(f'{dia}: {get_dia_semana(dia)}')
