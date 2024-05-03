import csv

data = [
    ['Nurik' ,'Kuandyk' ,  87964617856],
    ['Saparbek' ,'Rakhmanberdiev' ,87142876154],
    ['Jolbarys' ,'Tolebekov' ,87783875474],
    ['Duman' , 'Rustamov',87776019863]
]

with open('sample.csv' , 'w' , newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['first_name' ,'second_name' ,'phone_number'])

    for row in data:
        writer.writerow(row)