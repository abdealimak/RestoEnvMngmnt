import json

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.orders = 0

    def record_order(self, count):
        self.orders += count

    def popularity_rank(self):
        return self.orders

    def revenue_report(self):
        return self.price * self.orders

    @staticmethod
    def save_menu_data(summary_data, filename="menu_summary.json"):
        with open(filename, "w") as file:
            json.dump(summary_data, file, indent=4)
