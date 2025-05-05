#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction = 0

  def add_item(self, title, price, quanitity=1):
    self.total += price * quanitity
    self.items.extend([title] * quanitity)
    self.last_transaction = price * quanitity

  def apply_discount(self):
    if self.discount > 0:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    if self.total < 0:
      self.total = 0
