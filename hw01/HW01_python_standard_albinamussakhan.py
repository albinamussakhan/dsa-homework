#Стандарт
cities  = [" almaty", "Astana", "SHYMKENT", "Almaty ", "karaganda", "astana", "Almaty", "Aktobe", "Astana", "shymkent", "Almaty", "Atyrau"]
amounts = ["15990", "4500", "32000", "870", "12500", "56000", "2300", "9900", "18000", "7400", "41000", "3300"]
paid    = [True, True, False, True, True, False, True, True, True, False, True, True]
days    = ["пн", "пн", "вт", "вт", "ср", "ср", "чт", "пт", "пт", "сб", "сб", "вс"] 
#1
amounts=[int(amounts) for amounts in amounts]
cities=[cities.strip().capitalize() for cities in cities]
sum_ast=0
sum_alm=0
for amount, city in zip(amounts, cities):
    if city=="Astana":
     sum_ast+=amount
    if city=="Almaty":
      sum_alm+=amount
print(sum_ast,sum_alm)
#2
max_amt=0
city='none'
idx=0
for (indx, amount), status, city in zip(enumerate(amounts), paid,cities):
        if amount>max_amt and status:
           max_amt=amount
           idx=indx
           
print(f"Index: {idx}, City: {cities[idx]}")
#3
total=0
weekend=0
cnt=0
for amount, day in zip(amounts, days):
    total+=amount
    if day=="сб" or day=="вс":
        cnt+=1
        weekend+=amount
percent_d=(cnt/len(days))*100
percent_amnt=(weekend/total)*100
print(f"Share in amount: {percent_amnt}%, Share in days: {percent_d}%")

#4
wallet=0
saving=15000
months=0
while wallet<400000:
    wallet+=saving
    months+=1
    saving+=1000
    
print(months)
    