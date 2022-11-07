sum = 0
ticket = int(input("Сколько билетов приобретем?"))
for i in range(ticket):
    print("Возраст", i+1, "участника?")
    age = int(input())
    if 18 <= age <= 25:
        sum += 990
    elif age > 25:
        sum += 1390
    else:
        continue
if ticket > 3:
    sum *= 0.9
print("Всего к оплате:", sum)
