def show_even(numbers: list = []):
    if len(numbers) > 10:
        print("Lista jest za długa")
    else:
        for number in numbers:
            if number % 2 == 0:
                print(number)


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
show_even(test)
