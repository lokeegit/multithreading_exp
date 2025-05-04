import threading
import random
import time

MAX_THREADS = 4
thread_count = 0
lock = threading.Lock()

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def threaded_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    left_result = []
    right_result = []

    def sort_left():
        nonlocal left_result
        left_result = threaded_quicksort(left)

    def sort_right():
        nonlocal right_result
        right_result = threaded_quicksort(right)

    global thread_count
    threads = []

    with lock:
        can_spawn = thread_count + 2 <= MAX_THREADS
        if can_spawn:
            thread_count += 2

    if can_spawn:
        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)
        t1.start()
        t2.start()
        threads.extend([t1, t2])
    else:
        left_result = threaded_quicksort(left)
        right_result = threaded_quicksort(right)

    for t in threads:
        t.join()
    with lock:
        thread_count -= len(threads)

    return left_result + [pivot] + right_result


if __name__ == "__main__":
    SIZE = 100000
    arr = [random.randint(0, 1000000) for _ in range(SIZE)]

    print(f"Sorting {SIZE} elements...\n")

    start = time.time()
    threaded_sorted = threaded_quicksort(arr.copy())
    threaded_time = time.time() - start
    print(f"Threaded quicksort time: {threaded_time:.4f} seconds")

    start = time.time()
    single_sorted = quicksort(arr.copy())
    single_time = time.time() - start
    print(f"Single-threaded quicksort time: {single_time:.4f} seconds")

    assert threaded_sorted == single_sorted, "Mismatch in sorting results!"
