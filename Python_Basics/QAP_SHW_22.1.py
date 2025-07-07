# Начальный код. Сложность O(n2). Задача: успростить код, сделать сложность O(n)
from typing import Any


def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates


# Решение:

def find_duplicates(arr):
    # Инициализация множества для уникальных элементов и списка для дубликатов.
    seen = set()
    duplicates: list[Any] = []
    for item in arr:
        # Если элемент уже встречался, добавить в дубликаты.
        if item in seen:
            duplicates.append(item)
        else:
            # Иначе добавить в уникальные элементы.
            seen.add(item)
    # Возвращение списка дубликатов.
    return duplicates
