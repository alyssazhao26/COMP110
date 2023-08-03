""""Exercises functiosn for pytest."""

def sum(xs: list[float]) -> float:
    "returns the sum of float numbers in xs"
    sum_total: float = 0.0
    for index in range(0, len(xs), 1):
        sum_total += xs[index]
    return sum_total
