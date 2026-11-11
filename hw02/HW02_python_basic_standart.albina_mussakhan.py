
# 1
'''Тут мы пытаемся получить ключ от А и В по очереди, так как пока наш словарь пустой он возвращает 0 но потом А сохрянется со значением +1,
поэтому втрой раз при вызове у нас уже ключ 1+1=2 значит А : 2, а В:1 потому что его вызываем только раз
'''
r = {}
for c in ["A", "B", "A"]:
    r[c] = r.get(c, 0) + 1
print(r)
# 2
''' У насть список где есть пока 0 а наша функция просто добавляет 1 с конца,  из за того что мы свою функицию вызвали 2 раза, финальный
ответ должен быть [0, 1, 1]
'''
def f(x):
    x.append(1)
a = [0]; f(a); f(a); print(a)

# 3
''' Приводим наш словарь в единную форму а это нижние буквы, тут мы видим 2 Алматы и  дубликать не считаются поэтому длинна списка 2 
'''
s = {c.lower() for c in ["Almaty", "ALMATY", "Astana"]}; print(len(s))
# 4
''' Строим словарь с длинной на каждое слово, поэтому ab:2, abc:3 снова из за дубликатов ab:2 будет только один раз
'''
d = {k: len(k) for k in ["ab", "abc", "ab"]}; print(d)

# 5
''' Наша функиця выводит значение которое передали только если оно больше чем 0 но при этом нету return а значит будет возвращать None. 
Ответ должен быть: 5, None 
'''
def g(n):
    if n > 0:
        print(n)
x = g(5); print(x)



import csv
from pathlib import Path

# Загрузка
file = Path(__file__).with_name("orders.csv")

with open(file, encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

print("Всего строк:", len(rows))



# БАЗА
# 1. Функции

def to_num(s):
    s = str(s).replace(" ", "").replace(",", ".")
    if s == "":
        return 0
    return float(s)


def clean_city(s):
    s = s.strip().lower()

    cities = {
        "almaty": "Алматы",
        "astana": "Астана",
        "shymkent": "Шымкент",
        "алматы": "Алматы",
        "астана": "Астана",
        "шымкент": "Шымкент",
        "караганда": "Караганда",
        "актобе": "Актобе",
        "атырау": "Атырау"
    }

    if s in cities:
        return cities[s]

    return s.title()


# 2. Количество заказов по категориям

print("\nЗадание 2")

categories = {}

for row in rows:
    category = row["category"]

    if category not in categories:
        categories[category] = 0

    categories[category] += 1

result = sorted(categories.items(), key=lambda x: x[1], reverse=True)

for category, count in result:
    print(category, count)


# 3. Выручка и средний чек

print("\nЗадание 3")

revenue = {}
counts = {}

for row in rows:
    if row["status"] == "оплачен":
        category = row["category"]
        amount = to_num(row["amount"])

        if category not in revenue:
            revenue[category] = 0
            counts[category] = 0

        revenue[category] += amount
        counts[category] += 1

print(f"{'Категория':20} {'Выручка':15} {'Средний чек':15}")

for category in revenue:
    average = revenue[category] / counts[category]
    print(f"{category:20} {revenue[category]:15.2f} {average:15.2f}")


# 4. Количество заказов по месяцам

print("\nЗадание 4")

months = {}

for row in rows:
    month = row["order_date"][:7]

    if month not in months:
        months[month] = 0

    months[month] += 1

for month in sorted(months):
    print(month, months[month])



# СТАНДАРТ

# 5. Выручка по месяцам

print("\nЗадание 5")

monthly_revenue = {}

for row in rows:
    if row["status"] == "оплачен":
        month = row["order_date"][:7]
        amount = to_num(row["amount"])

        if month not in monthly_revenue:
            monthly_revenue[month] = 0

        monthly_revenue[month] += amount

for month in sorted(monthly_revenue):
    print(month, monthly_revenue[month])

september = monthly_revenue.get("2026-09", 0)
october = monthly_revenue.get("2026-10", 0)

if september != 0:
    change = (october - september) / september * 100
    print(f"Изменение: {change:.2f}%")


# 6. Доля отменённых заказов по городам

print("\nЗадание 6")

total = {}
cancelled = {}

for row in rows:
    city = clean_city(row["city"])

    if city not in total:
        total[city] = 0
        cancelled[city] = 0

    total[city] += 1

    if row["status"] == "отменён":
        cancelled[city] += 1

for city in total:
    percent = cancelled[city] / total[city] * 100
    print(city, f"{percent:.2f}%")


# 7. Топ-5 клиентов по выручке

print("\nЗадание 7")

customers = {}

for row in rows:
    if row["status"] == "оплачен":
        customer = row["customer_id"]
        amount = to_num(row["amount"])

        if customer not in customers:
            customers[customer] = 0

        customers[customer] += amount

top = sorted(customers.items(), key=lambda x: x[1], reverse=True)

for customer, amount in top[:5]:
    print(customer, amount)


# 8. Уникальные клиенты по городам

print("\nЗадание 8")

city_customers = {}

for row in rows:
    city = clean_city(row["city"])
    customer = row["customer_id"]

    if city not in city_customers:
        city_customers[city] = set()

    city_customers[city].add(customer)

for city in city_customers:
    print(city, len(city_customers[city]))
