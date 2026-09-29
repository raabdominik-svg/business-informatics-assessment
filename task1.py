cart_total = 14500
shipping_fee = 0

if cart_total < 10000:
    shipping_fee = 2000
elif cart_total <= 20000:
    shipping_fee = 1000
else: 
    shipping_fee = 0

final_price = cart_total + shipping_fee
print("Your total pay is: " + str(final_price) + " HUF")
