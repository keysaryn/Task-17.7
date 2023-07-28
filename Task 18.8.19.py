sum_price = 0
free = 0

amount_ticket = range(int(input("Введите количество билетов которые хотите приобрести: ")))

for i in amount_ticket:
    age = int(input(f"\nВведите возраст для {i+1} посетителя: "))

    if age < 18:
        print("\n\t\tПосетителям до 18 вход бесплатный!")

    elif 18 <= age < 25:
        sum_price += 990

    elif age >= 25:
        sum_price += 1390

if len(amount_ticket) > 3:
    print("\nВам доступна 10% скидка")
    sum_price = sum_price * 90 / 100
    print(f"\nСумма с учетом скидки за {len(amount_ticket)} посетителей: {sum_price}")

if len(amount_ticket) < 3:
    print(f"\nСумма за {len(amount_ticket)} посетителей: {sum_price}")
