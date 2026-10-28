# Module 10: Inventory List Manager 
# Reflection 1: What suprised me the most about lists in python:
# That if you append the same item to the list twice and then remove it, the orginal one will be the one that is removed and not the one at the end of the list.
# Reflection 2: Describe one real business situation: 
#  If you are in a finance job you will have to find the in flow of the stock through lists because the data is flying out at very fast speeds. This is because their are programs that are doing large amount of trades per second. 
print("--- Exercise 1: Build the List ---")

inventory = ["pen", "notebook", "stabler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate the index of the middle item
print(inventory[middle]) # middle item

print("--- Exercise 3: Slicing practice ---")
print(inventory[0:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every other item

print("--- Exercise 4: Modifying the List ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeErro caught:", error)
    print("Tuples protect coordinateds: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumalator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340,127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales)/len(high_sales):.2f}")

