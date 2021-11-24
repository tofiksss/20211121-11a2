a = float(input('pirmās malas garums: '))  
b = float(input('otrās malas garums: '))  
c = float(input('trešās malas garums: '))  
#2. aprēķina pusi no perimetra
P=(a+b+c)/2 
#3. aprēķina laukumu
laukums=(P*(P-a)*(P-b)*(P-c)) ** 0.5 
print("Trīsstūra laukums ir:", laukums)