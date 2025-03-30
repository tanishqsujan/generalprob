def max_product_pair(arr):
    if len(arr) < 2:
        return None  

    arr.sort()
    
    max1, max2 = arr[-1], arr[-2]  
    min1, min2 = arr[0], arr[1]  

    if max1 * max2 > min1 * min2:
        return (max1, max2)
    else:
        return (min1, min2)

arr = [-10, -20, 1, 3, 5, 7, 6]
print(max_product_pair(arr))  
