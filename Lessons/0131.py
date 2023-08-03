"""While Loops by finding low value in string"""

card: str = "5135"

card_idx: int = 0
low_card: int = int(card[0])

while card_idx < 4:
    current_card: int = int(card[card_idx])
    if (low_card > current_card):
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)
