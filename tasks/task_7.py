print("Добро пожаловать в игру \"Камень-Ножницы-Бумага\"!")
player_1_name = input("Игрок 1, введите свое имя: ")
player_2_name = input("Игрок 2, введите свое имя: ")

player_1_ans = input(player_1_name + ": ")
player_2_ans = input(player_2_name + ": ")
while player_2_ans and player_1_ans != "камень" or "ножницы" or "бумага":
    if player_2_ans != ("камень" or "ножницы" or "бумага"):
        print(player_2_ans, "соблюдайте правила игры. Начнем игру заново!")
    elif player_1_ans != ("камень" or "ножницы" or "бумага"):
        print(player_1_ans, "соблюдайте правила игры. Начнем игру заново!")
    else:
        print("ПРЕДУПРЕЖДЕНИЕ: Пожалуйста соблюдайте правила игры. Начнем игру заново!")
