# База
cities  = [" almaty", "Astana", "SHYMKENT", "Almaty ", "karaganda", "astana", "Almaty", "Aktobe", "Astana", "shymkent", "Almaty", "Atyrau"]
amounts = ["15990", "4500", "32000", "870", "12500", "56000", "2300", "9900", "18000", "7400", "41000", "3300"]
paid    = [True, True, False, True, True, False, True, True, True, False, True, True]
days    = ["пн", "пн", "вт", "вт", "ср", "ср", "чт", "пт", "пт", "сб", "сб", "вс"] , 
 #1
cities_clean=[cities.strip().capitalize() for cities in cities]
print(cities_clean)
#2
amounts_init=[int(amount) for amount in amounts]
print(amounts_init)
#3
orders=0
total_sum=0
avg=0
for i in amounts_init:
     orders+=1
     total_sum+=i
avg=total_sum/orders
print(orders)
print(total_sum)
print(round(avg))
#4
unpaid=0 
unpaid_amnt=0
idx=0
for i in paid:
     if not i:
          unpaid+=1
          unpaid_amnt+=amounts_init[idx]
     idx+=1
    
print(unpaid)
print(unpaid_amnt)
#5
for city, amount, status in zip(cities_clean, amounts_init, paid):
    if status: status='Paid' 
    else: status="Unpaid"
    print(f"Город: {city} | Сумма: {amount} | Статус: {status}")