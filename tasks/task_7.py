print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")
player_1_name = input("Игрок 1, введите свое имя: ")
player_2_name = input("Игрок 2, введите свое имя: ")
variable = ["ножницы", "бумага", "камень"]
while True:
    print()
    player_1_ans = input(player_1_name + ": ")
    player_2_ans = input(player_2_name + ": ")

    if player_1_ans == "камень" and player_2_ans == "ножницы":
        print("Поздравляем! Победитель -", player_1_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "ножницы":
        print("Поздравляем! Победитель -", player_2_name + "!")

    elif player_1_ans == "камень" and player_2_ans == "бумага":
        print("Поздравляем! Победитель -", player_2_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "бумага":
        print("Поздравляем! Победитель -", player_1_name + "!")

    elif player_1_ans == "ножницы" and player_2_ans == "бумага":
        print("Поздравляем! Победитель -", player_1_name + "!")
    elif player_2_ans == "ножницы" and player_1_ans == "бумага":
        print("Поздравляем! Победитель -", player_2_name + "!")

    elif player_1_ans != variable[0 or 1 or 2] \
            and player_2_ans != variable[0 or 1 or 2]:
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте"
              " правила игры. Начнем игру заново!")

    elif player_1_ans != variable[0 or 1 or 2]:
        print(player_1_name, "соблюдайте правила игры."
                             " Начнем игру заново!")
    elif player_2_ans != variable[0 or 1 or 2]:
        print(player_2_name, "соблюдайте правила игры."
                             " Начнем игру заново!")
    elif player_1_ans == "бумага" and player_2_ans == "бумага":
        print("Ничья! Продолжайте играть")

    elif player_1_ans == "камень" and player_2_ans == "камень":
        print("Ничья! Продолжайте играть")
    elif player_1_ans == "ножницы" and player_2_ans == "ножницы":
        print("Ничья! Продолжайте играть")
    ext = input("Хотите сыграть еще раз? (да/нет): ")
    if ext == "нет":
        print("До встречи!")
        break
