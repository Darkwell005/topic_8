print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player_1_name = input("Игрок 1, введите свое имя: ")
player_2_name = input("Игрок 2, введите свое имя: ")
variables = ["камень", "ножницы", "бумага"]

congratulatory_message = "Поздравляем! Победитель -"

while True:
    print()
    player_1_ans = input(player_1_name + ": ")
    player_2_ans = input(player_2_name + ": ")

    if player_1_ans == "камень" and player_2_ans == "ножницы":
        print(congratulatory_message, player_1_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "ножницы":
        print(congratulatory_message, player_2_name + "!")
    elif player_1_ans == "камень" and player_2_ans == "бумага":
        print(congratulatory_message, player_2_name + "!")
    elif player_2_ans == "камень" and player_1_ans == "бумага":
        print(congratulatory_message, player_1_name + "!")

    elif player_1_ans == "ножницы" and player_2_ans == "бумага":
        print(congratulatory_message, player_1_name + "!")
    elif player_2_ans == "ножницы" and player_1_ans == "бумага":
        print(congratulatory_message, player_2_name + "!")

    elif player_1_ans not in variables and\
            player_2_ans not in variables:
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте"
              " правила игры. Начнем игру заново!")
    elif player_1_ans not in variables:
        print(player_1_name, "соблюдайте правила игры."
                             " Начнем игру заново!")
    elif player_2_ans not in variables:
        print(player_2_name, "соблюдайте правила игры."
                             " Начнем игру заново!")

    elif player_1_ans == player_2_ans:
        print("Ничья! Продолжайте играть")
    if player_1_ans in variables and player_2_ans in variables:
        ext = input("Хотите сыграть еще раз? (да/нет): ")
        if ext == "нет":
            print("До встречи!")
            break
