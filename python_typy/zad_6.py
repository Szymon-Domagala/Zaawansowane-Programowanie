def update_list(lst1: list = [1], lst2: list = [2]) -> list:
    new_list = []
    for num in lst1:
        if num not in lst2:
            new_list.append(num ** 3)
    for num in lst2:
        if num not in lst1:
            new_list.append(num ** 3)        
    return new_list

test = update_list([1,2,3],[3,4])
for num in test:
    print(num)