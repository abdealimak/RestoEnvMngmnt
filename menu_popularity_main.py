import matplotlib.pyplot as plt
from menu_item_class import MenuItem
from menu_utils import load_sales_from_csv, load_order, append_sale_to_csv

CSV_FILE = "menu_sales.csv"

# Add new sales entry
def add_new_sale():
    try:
        dish = input("Enter dish name: ").strip()
        price = float(input("Enter price: "))
        orders = int(input("Enter number of orders: "))

        # Validate input directly in load_order
        load_order(dish, price, orders)
        append_sale_to_csv(CSV_FILE, dish, price, orders)

        print("Sale added successfully!\n")
    except ValueError as e:
        print("Error:", e, "\n")

# Show most popular dishes
def show_popular_dishes():
    sales_data = load_sales_from_csv(CSV_FILE)
    menu_items = []

    for dish, data in sales_data.items():
        item = MenuItem(dish, data["price"])
        item.record_order(data["orders"])
        menu_items.append(item)

    menu_items.sort(key=lambda x: x.orders, reverse=True)

    print("\n--- Most Popular Dishes ---")
    for item in menu_items:
        print(f"{item.name}: {item.orders} orders")

    # Save summary as JSON
    summary = {}
    for item in menu_items:
        summary[item.name] = {
            "orders": item.orders,
            "revenue": item.revenue_report()
        }
    MenuItem.save_menu_data(summary)
    print("\nSummary saved to menu_summary.json\n")

# Show revenue summary
def show_revenue_summary():
    sales_data = load_sales_from_csv(CSV_FILE)
    menu_items = []

    for dish, data in sales_data.items():
        item = MenuItem(dish, data["price"])
        item.record_order(data["orders"])
        menu_items.append(item)

    print("\n--- Revenue Summary ---")
    for item in menu_items:
        print(f"{item.name}: ₹{item.revenue_report()}")
    print()

# Show popularity chart
def show_popularity_chart():
    sales_data = load_sales_from_csv(CSV_FILE)
    menu_items = []

    for dish, data in sales_data.items():
        item = MenuItem(dish, data["price"])
        item.record_order(data["orders"])
        menu_items.append(item)

    menu_items.sort(key=lambda x: x.orders, reverse=True)

    dish_names = [item.name for item in menu_items]
    order_counts = [item.orders for item in menu_items]

    plt.figure()
    plt.barh(dish_names, order_counts)
    plt.xlabel("Number of Orders")
    plt.ylabel("Dish Name")
    plt.title("Restaurant Menu Popularity Chart")
    plt.tight_layout()
    plt.show()

# Main CLI menu
def main_menu():
    while True:
        print("Restaurant Menu Analyzer")
        print("1. Add new sales entry")
        print("2. View most popular dishes")
        print("3. View revenue summary")
        print("4. Show popularity chart")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_new_sale()
        elif choice == "2":
            show_popular_dishes()
        elif choice == "3":
            show_revenue_summary()
        elif choice == "4":
            show_popularity_chart()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()