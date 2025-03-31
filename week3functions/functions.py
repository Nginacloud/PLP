def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (discount_percent * price/100)
    return price

try:
    price = float(input("Enter Original Price: "))
    discount_percent = float(input("Enter Discount: "))

    if price < 0 or discount_percent < 0:
        print("Error: no non-negative values")
    else:
        final_price = calculate_discount(price, discount_percent)
        print("Final Price: ", final_price)

except ValueError:
    print("Error: Enter valid numeric values")
