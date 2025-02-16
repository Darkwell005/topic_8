print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")

player_1_name = input("Игрок 1, введите свое имя: ")
player_2_name = input("Игрок 2, введите свое имя: ")
variables = ["камень", "ножницы", "бумага"]

congratulatory_message = "Поздравляем! Победитель -"
warning_msg = "ПРЕДУПРЕЖДЕНИЕ:"
rules_msg = "соблюдайте правила игры. Начнем игру заново!"

while True:
    print()
    player_1_ans = input(player_1_name + ": ")
    player_2_ans = input(player_2_name + ": ")

    if (player_1_ans not in variables
            and player_2_ans not in variables):
        print(warning_msg, "Пожалуйста", rules_msg)
        continue
    elif player_1_ans not in variables:
        print(player_1_name, rules_msg)
        continue
    elif player_2_ans not in variables:
        print(player_2_name, rules_msg)
        continue
    elif player_1_ans == player_2_ans:
        print("Ничья! Продолжайте играть")
        continue

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

    ext = input("Хотите сыграть еще раз? (да/нет): ")
    if ext == "нет":
        print("До встречи!")
        break
