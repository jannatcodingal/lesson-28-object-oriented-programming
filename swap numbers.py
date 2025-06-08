a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
def swap_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c
result = swap_numbers(a, b, c)
print("After swapping: a =", result[0], ", b =", result[1], ", c =", result[2])