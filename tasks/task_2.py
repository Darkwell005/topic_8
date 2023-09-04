numbers = ["21", "85", "150", "190", "135", "515", "80"]

for i in numbers:
    i: int = int(i)  # Отличное решение

    # Давайте улучшим, чтобы было if, elif и elif
    if 150 < i < 500:
        continue
    if i >= 500:
        break
    if i % 5 == 0:
        print(i)
