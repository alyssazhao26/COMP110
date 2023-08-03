
A: str = "012"
idx: int = 0
b: int = 0

while idx < len(A):
    b = int(A[idx])

    while b > 0:
        print(b)
        b = b - 1
    idx = idx + 1  

print(b)