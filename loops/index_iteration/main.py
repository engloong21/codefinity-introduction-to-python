prices = [29.99, 45.50, 12.75, 38.20]

# Iterate over the list of prices using range(len())
for cost in range(len(prices)):
    if cost == 0:
        factor = 0.10
    elif cost == 1:
        factor = 0.20
    elif cost == 2:
        factor = 0.15
    elif cost == 3:
        factor = 0.05
        
    # Apply the discount by reducing the price
    prices[cost] -= prices[cost] * factor
    print(f"New price of item {cost + 1}: ${prices[cost]:.2f}")

print(f"Updated price for item {cost}: ${prices[cost]:.2f}")
