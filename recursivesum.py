def algo(arr):
    print(f"{arr}")
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + algo(arr[1:])

total = algo([1, 2, 3, 4])
print(total)