def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - 1 - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def binary_search(lst, x):
    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high =  mid - 1
        else:
            return mid
    return -1

lst = [64, 34, 25, 12, 22, 11, 90]
x = 22

sorted_lst = bubble_sort(lst)
result = binary_search(sorted_lst, x)

print(f"Отсортированный список: {sorted_lst}")
print(f"Результат двоичного поиска: {result}")

def binary_search(element, lst):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (high + low) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            low = mid +1
        else:
            high = mid -1

    return -1


def main():
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    # Применяем сортировку методом пузырьковой сортировки
    sorted_list = bubble_sort(unsorted_list.copy())
    print("Отсортированный список:", sorted_list)

    # Применяем двоичный поиск
    element_to_search = 64
    result = binary_search(element_to_search, sorted_list)

    if result != -1:
        print(f"Элемент {element_to_search} найден по индексу {result}")
    else:
        print(f"Элемент {element_to_search} не найден в списке")


if __name__ == "__main__":
    main()
