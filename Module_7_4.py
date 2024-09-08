team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = round(((team1_time + team2_time)/tasks_total),1)

#challenge_result = 'Победа команды Волшебники данных!'
if score1 > score2 or score1 == score2 and team1_time > team2_time:
   challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


#%
print('В команде Мастера кода участников: %s!' %team1_num)
print('В команде Волшебников данных участников: %s!' %team2_num)
print('Итого сегодня в командах участников: %(name1)s и %(name2)s!' %{'name1':team1_num, 'name2':team2_num})

#format()
print('Команда Мастера кода решила задач: {}!'.format(score1))
print('Мастера кода решили задачи за {}!'.format(team1_time))
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {}!'.format(team2_time))

#f-строк
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')