data_types: list = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]

for i in data_types:
    if type(i) == float:
        continue
    elif type(i) == str:
        continue
    print("Элемент:", i, "Тип:", type(i))

# -------------------------
# https://github.com/Darkwell005/topic_3

# Цикл
# в теле цикла if
# в теле if print
