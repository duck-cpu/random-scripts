def algo(arr, count=0):
    print(count)
    count += 1
    if len(arr) == 0:
        return count
    else:
        return algo(arr[1:], count) 
       
total = algo([1, 2, 3, 4]) 