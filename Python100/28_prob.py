import random,itertools

deck = list(itertools.product(range(1,14),["Spades","Hearts","Diamonds","Clubs"]))
result = random.choice(deck)

print(result)