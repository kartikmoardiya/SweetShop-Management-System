import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from operations_function import SweetOperator

def print_menu():
    print("""
============================
      SWEET SHOP MENU
============================
1. Add Sweet
2. Delete Sweet
3. View Sweets
4. Purchase Sweet
5. Restock Sweet
6. Search/Sort Sweets
7. Exit
""")

def print_sweets(sweets):
    if not sweets:
        print("-- No sweets to show --")
        return
    print(f"{'ID':<5}{'Name':<20}{'Category':<12}{'Price':<8}{'Quantity':<8}")
    print("-"*53)
    for sweet in sweets:
        print(f"{sweet.id:<5}{sweet.name:<20}{sweet.category:<12}{sweet.price:<8}{sweet.quantity:<8}")

def main():
    shop = SweetOperator()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            try:
                id = int(input("Enter Sweet ID (integer): "))
                name = input("Enter Sweet Name: ").strip()
                category = input("Enter Sweet Category (chocolate/candy/pastry): ").strip()
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                result = shop.add_sweet(id, name, category, price, quantity)
                print(result)
            except Exception as e:
                print("Invalid input. Please try again.")

        elif choice == '2':
            try:
                id = int(input("Enter Sweet ID to delete: "))
                result = shop.delete_sweets(id)
                print(result)
            except Exception as e:
                print("Invalid input. Please try again.")

        elif choice == '3':
            sweets = shop.view_sweets()
            print_sweets(sweets)

        elif choice == '4':
            name = input("Enter Sweet Name to purchase: ").strip()
            try:
                quantity = int(input("Enter Quantity to purchase (default 1): ") or "1")
            except:
                quantity = 1
            result = shop.sweet_purchase(name, quantity)
            print(result)

        elif choice == '5':
            name = input("Enter Sweet Name to restock: ").strip()
            try:
                quantity = int(input("Enter Quantity to restock: "))
            except:
                print("Invalid quantity.")
                continue
            result = shop.restock_sweets(name, quantity)
            print(result)

        elif choice == '6':
            print("Sort by: id, name, category, price, quantity")
            sort_by = input("Enter sort attribute: ").strip()
            result = shop.sweet_search(sort_by)
            if isinstance(result, str):
                print(result)
            else:
                print_sweets(result)

        elif choice == '7':
            print("Thanks for visiting the Sweet Shop!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 7.")

        input("\nPress Enter to continue... ")


if __name__ == "__main__":
    main()