#折半查找
def bisearch(lst, key): 
    low, high = 0, len(lst)-1 
    while low <= high: #范围内还有元素 
        mid = (low + high)//2 
        if key == lst[mid].key: 
            return lst[mid].value 
        if key < lst[mid].key: 
            high = mid - 1 #在低半区继续 
        else: 
            low = mid + 1  #在高半区继续