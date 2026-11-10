import re
import math


def is_palindrome(text: str) -> bool:
    text = text.replace(" ", "").lower()
    new_text = text[::-1]
    return text == new_text


def fibonacci(n: int) -> int:
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def count_vowels(text: str) -> int:
    vowels = {"a", "ą", "e", "ę", "i", "o", "u", "ó", "y"}
    quantity = 0
    text = text.lower()
    for chr in text:
        if chr in vowels:
            quantity += 1
    return quantity


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("Znizka ma byc w przedziale 0-1")
    return price - price * discount


def flatten_list(nested_list: list) -> list:
    new_list = []
    for elem in nested_list:
        if isinstance(elem, list):
            elem = flatten_list(elem)
            new_list.extend(elem)
        else:
            new_list.append(elem)
    return new_list


def word_frequencies(text: str) -> dict:
    frequency_dict = {}
    if not text:
        return frequency_dict
    words = re.split(r'[ ,.!]+', text.lower())
    for word in words:
        if not word:
            continue
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    

    end = math.isqrt(n)
    for i in range(3, end + 1, 2):
        if n % i == 0:
            return False
    return True
