def calculate_shipping(cart_total):
  if cart_total < 10000:
    return cart_total + 2000
  elif cart_total <= 20000:
    return cart_total + 1000
  else:
    return cart_total

print(calculate_shipping(5000))
print(calculate_shipping(15000))
print(calculate_shipping(25000))
