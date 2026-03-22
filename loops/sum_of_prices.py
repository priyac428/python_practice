# Topic : Sum of Prices
d = {"milk":22,
     "sugar":43,
    "pen":7,
    "salt":12,
   "maida":57} 
total = 0
for price in d.values():
    total+=price
print(f"total price {total}")