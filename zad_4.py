def show_second(numbers : list = []):
    if len(numbers) > 10:
        print("Lista jest za długa")
    else:
        for i in range (10):
            if i % 2 == 1:
                print(numbers[i])

test = [1,2,3,4,5,6,7,8,9,10]
show_second(test)