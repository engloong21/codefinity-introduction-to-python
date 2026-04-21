# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Function to calculate revenue
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, qty in zip(prices, quantities_sold):
        revenue.append(price * qty)
    return revenue

# Function to format output
def formatted_output(revenues):
    revenues.sort(key=lambda x: x[0]) # sortby product name
    for product, revenue in revenues:
        print(f"{product.lower()} has total revenue of ${revenue:.2f}")

# Calculate revenue
revenue = calculate_revenue(prices, quantities_sold)

# Combine products with revenue
revenue_per_product = list(zip(products, revenue))

# Output results
formatted_output(revenue_per_product)

# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")