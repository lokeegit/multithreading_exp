import threading
import time

def merge(left, right):
    result = []
    i = j = 0

    # Merge logic
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    t1 = threading.Thread(target=lambda: left.sort())
    t2 = threading.Thread(target=lambda: right.sort())

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(left, right)

# Example usage
import random

arr = [random.randint(0, 10000) for _ in range(10000)]

start = time.time()
sorted_arr = threaded_merge_sort(arr.copy())
print("Threaded sort time:", time.time() - start)

start = time.time()
arr.sort()
print("Single-threaded sort time:", time.time() - start)
