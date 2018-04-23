import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
# Examine the data
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#Merge cisits and cart
visits_to_cart = pd.merge(
  visits,
  cart,
  how = 'left')
print(len(visits_to_cart))

# Identify Missing cart_time
non_cart = visits_to_cart[visits_to_cart.cart_time.isnull()]
print(len(non_cart))
## 1652 user did not add anything to their cart

print(float(len(non_cart))/len(visits_to_cart))
# 81% of users  who did not place a t-shirt into a cart

# Merge cart and checkout
cart_to_checkout = pd.merge(
  cart,
  checkout,
  how = "left")

non_checkout = cart_to_checkout[cart_to_checkout.checkout_time.isnull()]
print(float(len(non_checkout))/len(cart_to_checkout))
# 20% of users who put a t-shirt in the cart but did not checkout

# Merge all data tables
all_data = pd.merge(
  visits,
  cart,
  how = 'left').merge(
  checkout,
  how = "left").merge(
  purchase,
  how = "left")
print(all_data.head())

# Users who made  made it to checkout, but did not make a purchase
cart_no_purchase = all_data[all_data.checkout_time.notnull() &
                            all_data.purchase_time.isnull()]
print(float(len(cart_no_purchase))/len(all_data))
# About 6% of users put an item in a cart but not a purchase

#Cool T-Shirts has the greatest issues of funneling users who visit the site 
# on to putting an item into their cart.

# Time from visit to purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean()) #average time to purchase
