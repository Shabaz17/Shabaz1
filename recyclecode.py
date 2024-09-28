import re
from datetime import datetime
import unittest

class RecyclingData:
    def __init__(self, recycling_id, item, quantity, date):
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if not re.match(r'\d{4}-\d{2}-\d{2}', date):
            raise ValueError("Date must be in YYYY-MM-DD format.")
        self.recycling_id = recycling_id
        self.item = item
        self.quantity = quantity
        self.date = date

    def __repr__(self):
        return (f"RecyclingData(recycling_id={self.recycling_id}, item='{self.item}', "
                f"quantity={self.quantity}, date='{self.date}')")


class RecyclingTracker:
    def __init__(self):
        self.recycling_entries = {}
        self.logging = []

    def create_recycling_data(self, recycling_id, item, quantity, date):
        if recycling_id in self.recycling_entries:
            raise ValueError("Recycling ID already exists.")
        self.recycling_entries[recycling_id] = RecyclingData(recycling_id, item, quantity, date)

    def read_recycling_data(self, recycling_id):
        return self.recycling_entries.get(recycling_id, None)

    def update_recycling_data(self, recycling_id, item=None, quantity=None, date=None):
        if recycling_id not in self.recycling_entries:
            raise ValueError("Recycling ID does not exist.")
        entry = self.recycling_entries[recycling_id]
        if item is not None:
            entry.item = item
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity must be a non-negative integer.")
            entry.quantity = quantity
        if date is not None:
            if not re.match(r'\d{4}-\d{2}-\d{2}', date):
                raise ValueError("Date must be in YYYY-MM-DD format.")
            entry.date = date

    def delete_recycling_data(self, recycling_id):
        if recycling_id not in self.recycling_entries:
            raise ValueError("Recycling ID does not exist.")
        del self.recycling_entries[recycling_id]

    def log_recycling_efforts(self, recycling_id):
        entry = self.read_recycling_data(recycling_id)
        if entry is None:
            raise ValueError("Recycling ID does not exist.")
        self.logging.append((entry, datetime.now()))

    def generate_recycling_reports(self):
        total_items = sum(entry.quantity for entry in self.recycling_entries.values())
        report = {
            'total_entries': len(self.recycling_entries),
            'total_quantity': total_items,
            'entries': list(self.recycling_entries.values()),
        }
        return report


def main():
    tracker = RecyclingTracker()

    while True:
        print("\n=== Campus Recycling Tracker ===")
        print("1. Create Recycling Data")
        print("2. Read Recycling Data")
        print("3. Update Recycling Data")
        print("4. Delete Recycling Data")
        print("5. Log Recycling Efforts")
        print("6. Generate Recycling Reports")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            recycling_id = input("Enter Recycling ID: ")
            item = input("Enter item: ")
            quantity = int(input("Enter quantity: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                tracker.create_recycling_data(recycling_id, item, quantity, date)
                print("Recycling data created successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            recycling_id = input("Enter Recycling ID to read: ")
            entry = tracker.read_recycling_data(recycling_id)
            if entry:
                print(entry)
            else:
                print("Recycling ID not found.")

        elif choice == '3':
            recycling_id = input("Enter Recycling ID to update: ")
            item = input("Enter new item (leave blank to keep current): ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            date = input("Enter new date (leave blank to keep current): ")

            try:
                tracker.update_recycling_data(
                    recycling_id,
                    item if item else None,
                    int(quantity) if quantity else None,
                    date if date else None
                )
                print("Recycling data updated successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            recycling_id = input("Enter Recycling ID to delete: ")
            try:
                tracker.delete_recycling_data(recycling_id)
                print("Recycling data deleted successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '5':
            recycling_id = input("Enter Recycling ID to log efforts: ")
            try:
                tracker.log_recycling_efforts(recycling_id)
                print("Recycling efforts logged successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '6':
            report = tracker.generate_recycling_reports()
            print("=== Recycling Report ===")
            print(f"Total Entries: {report['total_entries']}")
            print(f"Total Quantity: {report['total_quantity']}")
            for entry in report['entries']:
                print(entry)

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
