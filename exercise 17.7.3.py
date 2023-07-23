per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

payment = int(input('Введите сумму вклада: '))

profit_tkb = payment * per_cent.get('ТКБ') * 365 / 365 / 100
profit_skb = payment * per_cent.get('СКБ') * 365 / 365 / 100
profit_vtb = payment * per_cent.get('ВТБ') * 365 / 365 / 100
profit_sber = payment * per_cent.get('СБЕР') * 365 / 365 / 100

deposit = [round(profit_tkb, 2),round(profit_skb, 2),round(profit_vtb, 2),round(profit_sber, 2)]

print("Накопленные средства за год вклада в каждом из банков - ",deposit)
print("Максимальная сумма, которую вы можете заработать - ",max(deposit))