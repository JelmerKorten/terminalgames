dct = {"a":3, "b":2}
card = "a"
card_weight = dct.get(card)
dct.update({card:card_weight - 1})
print(dct)