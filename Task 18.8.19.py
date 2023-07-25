yang_price = 990
full_price = 1390
sum_price = 0

amount_ticket = int(input("Введите количество билетов которые хотите приобрести: "))

enter_age = int(input("Введите возраст: "))

if enter_age < 18:
    print("Лицам до 18 вход бесплатный!", list(range(0,amount_ticket)))

elif 18 >= enter_age < 25:
    print("")
    sum_price += yang_price



# if amount_ticket > 1:


# if amount_ticket > 3:
#     print("Вам доступна 10% скидка")
#     sum_order = sum_order * 90 / 100
#     print("Сумма с учетом скидки: ")


