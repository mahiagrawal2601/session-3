"list of product prices from flipkart"

prices = ['199.99','299.50','150']

float_prices = [float(price) for price in prices ]

total = sum(float_prices)

print("Total cart value: ", total)
print(float_prices)