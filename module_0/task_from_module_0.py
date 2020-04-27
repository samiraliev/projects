#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np

def game_core(number):
    '''Функция,которая ищет число наиболее быстрым способом'''
    count = 0
    left = 1
    right = 101
    predict = np.random.randint(left,right) # устанавливаем левые и правые границы интервала и загадываем
                                            # число на этом интервале    
    while number != predict: # пока мы не угадали
        count += 1 # Увеличиваем количество попыток на 1
        middle = (left + right) // 2 # устанавливаем середину интервада
        if number > predict: 
            left = predict # Устанавливаем новую левую границу, если загаданное число больше
            predict = (left + right) // 2 # новый прогноз будет осуществляться на сокращённом в 2 раза интерваде
        elif number < predict: 
            right = predict # Устанавливаем новую правую границу, если загаданное число меньше
            predict = (left + right) // 2
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = [] # список чисел, показывающих, за сколько попыток мы угадали число
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000)) # Симулируем 1000 попыток
    for number in random_array:
        count_ls.append(game_core(number)) # присоединяем количество попыток в список
    score = int(np.mean(count_ls)) # считаем среднее из успешных попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score) # Возвращаем результат и кайфуем
score_game(game_core_v2)


# In[ ]:




