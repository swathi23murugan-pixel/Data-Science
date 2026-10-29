def calculate_bill(prices, tax_rate=0.10, discount=0.20):
    subtotal = sum(prices)
    discount_amount = subtotal * discount
    amount = subtotal - discount_amount
    tax = amount * tax_rate
    total = amount + tax

    print("Subtotal:", format(subtotal, ".2f"))
    print("Discount:", format(discount_amount, ".2f"))
    print("Tax:", format(tax, ".2f"))
    print("Final total:", format(total, ".2f"))

prices = [100, 50]
calculate_bill(prices, tax_rate=0.10, discount=0.20)
