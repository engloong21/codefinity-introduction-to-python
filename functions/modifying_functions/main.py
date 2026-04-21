# Apply discount
def apply_discount(price, discount=0.05):
    return price * (1 - discount)

# Apply tax
def apply_tax(price, tax=0.07):
    return price * (1 + tax)

# Calculate total
def calculate_total(price, discount=0.05, tax=0.07):
    discounted_price = apply_discount(price, discount)
    total_price = apply_tax(discounted_price, tax)
    return total_price

# Using default values
default_total_price = calculate_total(120)

# Using custom keyword arguments
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)

# Output
print(f"Total cost with default discount and tax: ${default_total_price:.2f}")
print(f"Total cost with custom discount and tax: ${total_price_custom:.2f}")
