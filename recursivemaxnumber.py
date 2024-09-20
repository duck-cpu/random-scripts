def algo(arr, max_num):
    print(arr, max_num)
    if len(arr) == 0:
        return max_num
    else:
        if max_num < arr[0]:
            max_num = arr[0]
        return algo(arr[1:],max_num)
total = algo([7, 8, 4, 2, 6, 9, 1, 1],0)