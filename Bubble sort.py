def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"Pass {i + 1}, Iteration {j + 1}: {arr}")

# Generate a random list of integers for sorting
import random

random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

print("Sorting using Bubble Sort:")
bubble_sort(random_list)

print("Sorted list:", random_list)

# Test Bubble Sort with a list in reverse order
reverse_list = list(range(10, 0, -1))
print("\nOriginal list (in reverse order):", reverse_list)

print("Sorting reverse order list using Bubble Sort:")
bubble_sort(reverse_list)

print("Sorted list:", reverse_list)
