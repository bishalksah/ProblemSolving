# while purchasing a product, if the price is more than 1000, apply a discount of 10% and if the price is more than 5000, apply a discount of 20%. Calculate the final price after applying the discount.


price = float(input("Enter the price of the product: "))
if price > 5000:
    final_price = price - (price * 0.2)
elif price > 1000:
    final_price = price - (price * 0.1)
else:
    final_price = price
print("The final price after applying the discount is:", final_price)