#not fully my code, from textbook. **edited to display output 
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        total = quicksort(less) + [pivot] + quicksort(greater)

        return total
total = quicksort([10, 5, 2, 3, 5, 5, 2, 9, 20, 100, 1000, 500, 20, 33])

print(total)