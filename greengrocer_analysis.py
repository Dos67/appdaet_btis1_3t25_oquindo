#Data
raw_transactions = ["24.50", "12.00", "ERROR_CODE_4", "45.25", "N/A", "110.00", "-15.00", "5.75"]
warehouse_east = ["apples", "bananas", "oranges", "kale", "avocados"]
warehouse_west = ["bananas", "avocados", "blueberries", "kale", "mangoes"]
loyalty_points = {
    "Alice": [85, 90, 92],
    "Bob": [70, 65, 78],
    "Charlie": [95, 100, 92]
}

#Phase 1
clean_transactions = []
for transaction in raw_transactions:
    try:
        number = float(transaction)
        if number >= 0:
            clean_transactions.append(number)
    except:
        pass
print("=" * 40)
print("PHASE 1: Terminal Log Data Cleansing")
print("=" * 40)
print(f"Clean Transactions: {clean_transactions}")

total_revenue = sum(clean_transactions)
average_transaction = total_revenue / len(clean_transactions)
print(f"Total Revenue: {total_revenue}")
print(f"Average Transaction: {average_transaction}")

highest_transaction = clean_transactions[0]
for transaction in clean_transactions:
    if transaction > highest_transaction:
        highest_transaction = transaction
print(f"Highest Transaction: {highest_transaction}")

#Phase 2
east = set(warehouse_east)
west = set(warehouse_west)
#Union (all in east plus west without duplicate)
total_catalog = east | west
#Intersection (found in both sets)
shared_inventory = east & west
#Difference (items found only in east warehouse)
regional_exclusive = east - west
print("=" * 40)
print("PHASE 2: Warehouse Stock Reconciliation")
print("=" * 40)

print(f"Total Catalog: {total_catalog}")
print(f"Shared Inventory: {shared_inventory}")
print(f"Regional Exclusive: {regional_exclusive}")

#Phase 3
loyalty_points["Diana"] = [88, 85, 90]
loyalty_points["Bob"].append(82)
print("=" * 40)
print("PHASE 3: Customer Rewards & Loyalty gradebook")
print("=" * 40)
print(f"Loyalty Points + Diane: {loyalty_points}")
print("Average Loyalty Points ")

highest_average = 0
green_champion = ""

for customer, points in loyalty_points.items():
    average = sum(points) / len(points)
    print(f"{customer}: {round(average,1)}")
    if average > highest_average:
        highest_average = average
        green_champion = customer
print(f"Green Champion: {green_champion}")

if total_revenue > 200:
    print("Daily Sales Target: ACHIEVED")
else:
    print("Daily Sales Target: PENDING")
