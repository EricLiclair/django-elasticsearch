
import csv

def populate_db():
    with open('data.csv') as f:
        lines = csv.reader(file)
        for line in lines:
            name, price, quantity = line
            Product.objects.create(name=name, price=price, quantity=quantity)

populate_db()