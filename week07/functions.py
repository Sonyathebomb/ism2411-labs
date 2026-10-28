# 1. The first bug that I spotted was a syntax error. I found it from the traceback. Explaing the code to the duck tells me that I always need to double check what I am coding, and making sure I print one line at a time so I don't get confused if there is ever an error to pop up.
# 2. This function calculates a discounted price based on tier and price which are the inputs. It returnd a number that represents the final price after a discount. No they wouldn't be able to use this because they would not know what the valid tiers are.
# 3. I used AI to help me with the second error which was a index error. I didn't know what it meant so it helped me to realized that I needed to put a valid input from the list for the code to work.

# --- Exercise 1 ---
# Define the function

def calculate_tax(price, rate):
    return price * rate
# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on 100 at 7%: ${tax1:.2f}")
print(f"Tax on 250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

    # --- Exercise 3 ---
# write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# --- Exercise 6 ---

x = 100 # apple # Global 

def double_it():
    global x 
    # x = 999 # another apple (not the same as above)
    return x * 2

print(x)
print(double_it())
print(x)