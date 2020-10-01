#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")

def game_core_v3 (number):
    count = 0
    low = 0 #нижняя граница диапозона
    high = 101 #верхняя граница диапозона
    predict = (low + high) // 2 # ищем медиану диапозона для уменьшения области поиска
    while number != predict: 
        if number < predict:
            high = predict # проверка верхней границы диапозона
            predict = predict - ((high-low) // 2) # уменьшение последующей области поиска до медианы верхнего диапозона
        elif number > predict:
            low = predict # проверка нижней границы диапозона
            predict = predict + ((high-low) //2 ) # уменьшение последующей области поиска до медианы нижнего диапозона
        count += 1
    return(count) # выход из цикла, если угадали
score_game(game_core_v3)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[ ]:




