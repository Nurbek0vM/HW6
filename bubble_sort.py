def bibble_sort(lst):
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

sorted_lst = bibble_sort(lst)
result = binary_search(sorted_lst, x)

print(f"Отсортированный список: {sorted_lst}")
print(f"Результат двоичного поиска: {result}")