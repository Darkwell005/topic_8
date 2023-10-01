data_types: list = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]

# ---------------- №0 ----------------
for i in data_types:
    if type(i) == float:
        continue
    elif type(i) == str:
        continue
    print("Элемент:", i, "Тип:", type(i))

# ---------------- №1 ----------------
for i in data_types:
    if isinstance(i, float) or isinstance(i, str):
        continue
    print("Элемент:", i, "Тип:", type(i))

# ---------------- №2 ----------------

for item in data_types:
    # Можно сразу кортеж типов передать в isinstance()
    if isinstance(item, (float, str)):
        continue
    print("Элемент:", item, "Тип:", type(item))

# Лучше так
# ---------------- №3 ----------------
for item in data_types:
    if not isinstance(item, (float, str)):
        print("Элемент:", item, "Тип:", type(item))
