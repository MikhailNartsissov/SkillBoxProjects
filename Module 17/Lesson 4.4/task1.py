from random import randint


original_prices = [randint(-20, 20) for _ in range(10)]
new_prices = original_prices[:]
new_prices = [0 if price < 0 else price for price in new_prices]

print(original_prices)
print(new_prices)
print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
