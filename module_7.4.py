#Использование %
def number(team1_num = 5, team2_num = 6):
    print('В команде Мастера кода участников %s!' % (team1_num))
    print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))


#Использование format()
def time(score_2 = 40, team1_time = 42):
    print('Команда Волшебники данных решила задач: {}'.format(score_2))
    print('Волшебники данных решили задачи за {} с!'.format(team1_time))


#Использование f-строк
def challenger_result(team1_time = 1552.512, team2_time = 2153.31451, score_1 = 40 , score_2 = 42):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'

    print(f'Команды решили {score_1} и {score_2} задач.')
    print (f'Результат битвы: {result}')

def result_time_score(team1_time = 1552.512, team2_time = 2153.31451, score_1 = 40, score_2 = 42):
    tasks_total = score_1 + score_2
    result_time = (team1_time + team2_time) / tasks_total

    print (f'Сегодня было решено {tasks_total} задач, в среднем по {result_time} секунды на задачу!.')

number()
time()
challenger_result()
result_time_score()


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

