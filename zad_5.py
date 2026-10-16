def check_type(lst: list = [1], num: int = 1) -> bool:
    for element in lst:
        if element == num:
            return True
    return False

print(check_type([12,2,3],5))
print(check_type([12,2,3],2))