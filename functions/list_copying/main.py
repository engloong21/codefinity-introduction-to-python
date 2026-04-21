# 1. Define the function to apply discounts on product prices
def apply_discount(prices):
    # Create a copy of the `prices` list
    prices_copy = prices.copy()
    # Iterate through the list of prices using indexing
    for i in range(len(prices_copy)):
        # Apply a 10% discount if the price is greater than $2.00
        if prices_copy[i] > 2.00:
            prices_copy[i] *= 0.9
    return prices_copy

# 2. List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# 3. Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

# 4. Print the updated prices (no .2f on the whole list)
print(f"Updated product prices: {updated_prices}")