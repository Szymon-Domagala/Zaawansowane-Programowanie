def is_even(num: int = 2) -> bool:
    return num % 2 == 0

test1 = is_even(4)
test2 = is_even(3)

if test1:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
if test2:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")