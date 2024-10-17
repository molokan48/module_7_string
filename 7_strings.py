import random
team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = random.randint(6,10)
team2_num = random.randint(6,10)
score_1 = random.randint(40,85)
score_2 = random.randint(40,85)
team1_time = random.randint(1100 , 1600)
team2_time = random.randint(1100 , 1600)

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return  'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return  'Победа команды Волшебники Данных!'
    else:
        return  'Ничья'

print("В команде %s участников: %d ! " % (team1_name , team1_num))
print("В команде %s участников: %d ! " % (team2_name , team2_num))
print("Итого сегодня в командах участников: %d и %d !" %(team1_num , team2_num ))
print("{} решили задачи за {} с. !".format(team1_name , team1_time))
print("{} данных решили задачи за {} с. !".format(team2_name , team2_time))
print("Команда {} решила задач: {}".format(team2_name , score_2))
print("Команда {} решила задач: {}".format(team1_name , score_1))
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result()}")
print(f"Сегодня было решено {score_1 + score_2} задач, в среднем по"
      f" {round((team1_time + team2_time)/(score_1 + score_2) , 2 )} секунды на задачу!")
