import random
import timeit
from tabulate import tabulate

def insertion_sort(arr_):
    """Insertion sort an array in place and return it"""
    for i in range(1, len(arr_)):
        key = arr_[i]
        j = i - 1
        while j >= 0 and arr_[j] > key:
            arr_[j + 1] = arr_[j]
            j -= 1
        arr_[j + 1] = key
    return arr_


def merge_sort(arr_):
    arr = arr_[:]
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def bubble_sort(arr_):
    arr = arr_[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


small_data = [random.randint(0, 1000) for _ in range(100)]
medium_data = [random.randint(0, 1000) for _ in range(1000)]
large_data = [random.randint(0, 1000) for _ in range(10000)]

ts_insertion = timeit.timeit(lambda: insertion_sort(small_data), number=30)
ts_merge_sort = timeit.timeit(lambda: merge_sort(small_data), number=30)
ts_quick_sort = timeit.timeit(lambda: quick_sort(small_data), number=30)
ts_bubble_sort = timeit.timeit(lambda: bubble_sort(small_data), number=30)
ts_sorted = timeit.timeit(lambda: sorted(small_data), number=30)
ts_sort = timeit.timeit(lambda: small_data[:].sort(), number=30)

tm_insertion = timeit.timeit(lambda: insertion_sort(medium_data), number=30)
tm_merge_sort = timeit.timeit(lambda: merge_sort(medium_data), number=30)
tm_quick_sort = timeit.timeit(lambda: quick_sort(medium_data), number=30)
tm_bubble_sort = timeit.timeit(lambda: bubble_sort(medium_data), number=30)
tm_sorted = timeit.timeit(lambda: sorted(medium_data), number=30)
tm_sort = timeit.timeit(lambda: medium_data[:].sort(), number=30)

tl_insertion = timeit.timeit(lambda: insertion_sort(large_data), number=30)
tl_merge_sort = timeit.timeit(lambda: merge_sort(large_data), number=30)
tl_quick_sort = timeit.timeit(lambda: quick_sort(large_data), number=30)
tl_bubble_sort = timeit.timeit(lambda: bubble_sort(large_data), number=30)
tl_sorted = timeit.timeit(lambda: sorted(large_data), number=30)
tl_sort = timeit.timeit(lambda: large_data[:].sort(), number=30)

data = [
    ["Insertion Sort", ts_insertion, tm_insertion, tl_insertion],
    ["Merge Sort", ts_merge_sort, tm_merge_sort, tl_merge_sort],
    ["Quicksort", ts_quick_sort, tm_quick_sort, tl_quick_sort],
    ["Bubble Sort", ts_bubble_sort, tm_bubble_sort, tl_bubble_sort],
    ["Timsorted", ts_sorted, tm_sorted, tl_sorted],
    ["Timsort", ts_sort, tm_sort, tl_sort]
]

headers = ["Algorithm", "Small", "Medium", "Large"]

print(tabulate(data, headers, tablefmt="pipe"))

