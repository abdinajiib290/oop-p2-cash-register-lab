#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    try:
      if not isinstance(discount, int):
        raise ValueError
    except Exception:
      print("Not valid discount")
      discount = 0

    if discount < 0 or discount > 100:
      print("Not valid discount")
      discount = 0

    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)
    self.previous_transactions.append({
      'item': item,
      'price': price,
      'quantity': quantity
    })

  def apply_discount(self):
    if not self.discount:
      print("There is no discount to apply.")
      return

    discounted_total = self.total * (100 - self.discount) / 100
    # keep numeric total but when printing match expected format
    self.total = discounted_total
    # Format message without unnecessary decimal when whole number
    if float(self.total).is_integer():
      total_str = str(int(self.total))
    else:
      total_str = str(self.total)
    print(f"After the discount, the total comes to ${total_str}.")

  def void_last_transaction(self):
    if not self.previous_transactions:
      return

    last = self.previous_transactions.pop()
    item = last['item']
    price = last['price']
    quantity = last['quantity']

    self.total -= price * quantity
    # remove the last `quantity` occurrences of item from self.items
    to_remove = quantity
    i = len(self.items) - 1
    while i >= 0 and to_remove > 0:
      if self.items[i] == item:
        del self.items[i]
        to_remove -= 1
      i -= 1

