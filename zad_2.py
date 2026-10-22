def update_list_v1(numbers: list = []):
    if len(numbers) > 5:
        print("Lista jest za długa")
    else:
        new_list = []
        for number in numbers:
            new_list.append(number * 2)
        return new_list


def update_list_v2(numbers: list = []):
    if len(numbers) > 5:
        print("Lista jest za długa")
    else:
        new_list = [number * 2 for number in numbers]
        return new_list


test = [1, 2, 3, 4, 5]
print("Baza")
for number in test:
    print(number)
print("Wersja z for")
v1 = update_list_v1(test)
for number in v1:
    print(number)
print("Wersja z lista skladana")
v2 = update_list_v1(test)
for number in v2:
    print(number)
