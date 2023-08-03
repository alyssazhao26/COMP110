"""for loop """
pets: list[str] = ['Louie', 'Bo', 'Bear']

for animals in pets:
    print(f"Good boy, {animals}!")

# Tuples: fixed length 
# (x,y) Coordinates are the most frequent tuple

coordinate: tuple[float, float] = (1.0, 1.0)

# Range: intervals (made of integers) 
# format (a, b) -> a <= x < b
constructor: range(1, 5, 2) 
