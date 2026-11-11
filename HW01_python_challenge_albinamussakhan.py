#Челлендж 

cities  = [" almaty", "Astana", "SHYMKENT", "Almaty ", "karaganda", "astana", "Almaty", "Aktobe", "Astana", "shymkent", "Almaty", "Atyrau"]
amounts = ["15990", "4500", "32000", "870", "12500", "56000", "2300", "9900", "18000", "7400", "41000", "3300"]
paid    = [True, True, False, True, True, False, True, True, True, False, True, True]
days    = ["пн", "пн", "вт", "вт", "ср", "ср", "чт", "пт", "пт", "сб", "сб", "вс"] 
#1
cities=[cities.strip().capitalize() for cities in cities]
unique_cities=[]
for city in cities:
    if city not in unique_cities:
        unique_cities.append(city)
        
print(unique_cities)
      
cities=[city.strip().capitalize() for city in cities]
revenue_by_city=[]
amount=(int(amount) for amount in amounts)
total=0
for city, amount,status in zip(cities,amount,paid):
     if status and city :
         total+=amount
         revenue_by_city.append


#2
