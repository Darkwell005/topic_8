print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player_1_name = input("Игрок 1, введите свое имя: ")
player_2_name = input("Игрок 2, введите свое имя: ")


congratulatory_message = "Поздравляем! Победитель -"

while True:
    print()
    player_1_ans = input(player_1_name + ": ")
    player_2_ans = input(player_2_name + ": ")

    if player_1_ans == "камень" and player_2_ans == "ножницы":
        print(congratulatory_message, player_1_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "ножницы":
        print(congratulatory_message, player_2_name + "!")
        # в прошлой версии это правильно было реализовано,
        # значем сюда перенесли?
        ext = input("Хотите сыграть еще раз? (да/нет): ")
        if ext == "нет":
            print("До встречи!")
            break
    elif player_1_ans == "камень" and player_2_ans == "бумага":
        print(congratulatory_message, player_2_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "бумага":
        print(congratulatory_message, player_1_name + "!")

    elif player_1_ans == "ножницы" and player_2_ans == "бумага":
        print(congratulatory_message, player_1_name + "!")
    elif player_2_ans == "ножницы" and player_1_ans == "бумага":
        print(congratulatory_message, player_2_name + "!")

    # player_1_ans != ("бумага" or "ножницы" or "камень")
    # Это неправильная проверка, если Вы хотите сделать такую проверку,
    # она должна быть для каждого варианта отдельно:
    # (player_1_ans != "бумага"
    # or player_1_ans !=  "ножницы"
    # or player_1_ans != "камень")
    elif player_1_ans != ("бумага" or "ножницы" or "камень") and\
            player_2_ans != ("бумага" or "ножницы" or "камень"):
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте"
              " правила игры. Начнем игру заново!")
    elif player_1_ans != "бумага" or "ножницы" or "камень"\
            and player_2_ans == "бумага" or "ножницы" or "камень":
        print(player_1_name, "соблюдайте правила игры."
                             " Начнем игру заново!")
    elif player_2_ans != "бумага" or "ножницы" or "камень"\
            and player_1_ans == "бумага" or "ножницы" or "камень":
        print(player_2_name, "соблюдайте правила игры."
                             " Начнем игру заново!")
    # 2. Можно ли здесь улучшить?
    # Как-то не красиво, одно и то же повторяете 3 раза.
    elif player_1_ans == "бумага" and player_2_ans == "бумага":
        print("Ничья! Продолжайте играть")

    elif player_1_ans == "камень" and player_2_ans == "камень":
        print("Ничья! Продолжайте играть")
    elif player_1_ans == "ножницы" and player_2_ans == "ножницы":
        print("Ничья! Продолжайте играть")

"""
Анна
Макс
бумага
камень
да
камень
камень
бумага
ножницы
да
ок
кулак
ок
кулак
камень
кулак
ножницы
бумага
нет
"""
