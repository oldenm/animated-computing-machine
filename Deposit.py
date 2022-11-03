per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit_values = []
money = int(input("Сколько положим, Милорд?"))
for i in per_cent:
    deposit_values.append((per_cent[i]) * (money / 100))
max_deposit = max(deposit_values)
print("Максимальная сумма, которую вы можете заработать —", max_deposit)
