def print_names(names: list = []):
    if len(names) > 5:
        print("Lista jest za długa")
    else:
        for name in names:
            print(name)


print_names(["x", "z", "c", "a", "l"])
