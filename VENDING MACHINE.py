# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 17:27:25 2025

@author: trist
"""

class VendingMachine:
    def __init__(self):
        # Categories with items and their prices, now with labels
        self.categories = {
            'Drinks': {
                'A1': ('Pepsi', 5.00),
                'A2': ('Coke', 4.50),
                'A3': ('Miranda', 3.50),
                'A4': ('Sprite', 3.00),
                'A5': ('Root Beer', 6.00),
            },
            'Snacks': {
                'B1': ('Chips', 5.00),
                'B2': ('Candy', 4.75),
                'B3': ('Gum', 3.50),
                'B4': ('Bread', 6.50),
                'B5': ('Popcorn', 9.50),
            }
        }
        self.balance = 0.0

    def display_categories(self):
        print("Menu available:")
        for category in self.categories.keys():
            print(f"- {category}")

    def display_items(self, category):
        if category in self.categories:
            print(f"\nItems available in {category}:")
            for code, (item, price) in self.categories[category].items():
                print(f"{code}: {item} - ${price:.2f}")
        else:
            print("Invalid category selected.")

    def insert_money(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance:.2f}")

    def select_item(self, category, code):
        if category not in self.categories:
            print(f"Category '{category}' not available.")
            return

        if code not in self.categories[category]:
            print(f"Item with code '{code}' not available in {category}.")
            return
        
        item, item_price = self.categories[category][code]
        if self.balance >= item_price:
            self.balance -= item_price
            print(f"Dispensing {item} from {category}...")
            print(f"Remaining balance: ${self.balance:.2f}")
        else:
            print(f"Insufficient funds. Please insert ${item_price - self.balance:.2f} more.")

    def get_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0.0
        else:
            print("No balance to return.")


def run_vending_machine():
    vm = VendingMachine()
    
    while True:
        print("\n------ Welcome to Tan's Vending Machine ------")
        
        # Display the categories that are displayed
        vm.display_categories()
        
        # User can select category
        category_choice = input("\nSelect a category (Drinks/Snacks): ").capitalize()
        vm.display_items(category_choice)
        
        # User inserts the right amount money
        try:
            money_inserted = float(input("\nInsert money: $"))
            vm.insert_money(money_inserted)
            
            # User selects item by code (A1, B2, etc.)
            item_code = input(f"Select an item from {category_choice} by code (e.g., A1, B2): ").upper()
            vm.select_item(category_choice, item_code)
            
            # Ask if the customer wants to get change
            get_change = input("Would you like to get your change back? (yes/no): ").lower()
            if get_change == 'yes':
                vm.get_change()

            continue_shopping = input("Would you like to continue shopping? (yes/no): ").lower()
            if continue_shopping != 'yes':
                print("Thank you for using the Vending Machine. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the money.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    run_vending_machine()
