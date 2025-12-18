import csv
from datetime import date

def load_order(dish, price, orders):
    if not dish:
        raise ValueError("Dish name cannot be empty")
    if price <= 0:
        raise ValueError("Price must be greater than zero")
    if orders < 0:
        raise ValueError("Orders cannot be negative")
    
    return {
        "dish": dish,
        "price": price,
        "orders": orders
    }

def append_sale_to_csv(filename, dish, price, orders):
    today = date.today().isoformat()
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, dish, price, orders])

def load_sales_from_csv(filename):
    sales = {}
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dish = row["dish"]
            price = float(row["price"])
            orders = int(row["orders"])

            if dish in sales:
                sales[dish]["orders"] += orders
            else:
                sales[dish] = {"price": price, "orders": orders}
    return sales
