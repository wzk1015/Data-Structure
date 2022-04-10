#插入排序
def insert_sort(lst):
    for i in range(1,len(lst)): #[1,len)
        x = lst[i]
        j = i
        while j>0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]   #依次后移
            j -= 1
        lst[j] = x
#最坏情况：第i个数(i从2开始)比较i次，移动i+1次
#共比较Σi(i=2~n)=(n-1)(n+1)/2次
#共移动Σ(i+1)=(n-1)(n+4)/2次

#冒泡排序
def bubble_sort(lst):
    for i in range(len(lst)):   #[0,len)
        for j in range(1,len(lst)-i):   #[1,len-i) 第i趟排前n-i个元素(i从0开始)
            if lst[j-1].key > lst[j].key:
                lst[j-1],lst[j]=lst[j],lst[j-1]
#最坏情况：
#共比较Σ(n-i)次
#共移动3Σ(n-i)次（使用temp交换）


#选择排序
def select_sort(lst):
    for i in range(len(lst)-1): #[0,len-1) 
        k=i     #k是当前最小元素的位置
        for j in range(i,len(lst)): #[i,len) 第i趟排后n-i个元素(i从0开始)
            if lst[j].key < lst[k].key:
                k = j
        lst[i],lst[k]=lst[k],lst[i]



#快速排序（递归）
def qsort_rec(lst,l,r):
    if l>=r:    #分段内只有0或1个元素
        return
    i=l
    j=r
    pivot=lst[i]
    while i<j:
        while i<j and lst[j].key >= pivot.key:
            j -= 1  #从j向左找第一个小于pivot的元素
        if i<j:     
            lst[i] = lst[j] #小元素移到左边
            i += 1
        while i<j and lst[i].key >= pivot.key:
            i += 1  #从i向右找第一个大于pivot的元素
        if i<j:
            lst[j]=lst[i]
            j -= 1
        
    lst[i]=pivot    #pivot存入最终位置
    qsort_rec(lst,l,i-1)    #对左右两段分别进行下一趟快排
    qsort_rec(lst,i+1,r)
        
#快速排序（非递归）
def qsort_nonrec(lst,l,r):
    if l>=r:
        return
    stack=[l,r]
    while len(stack)!=0:
        low=stack.pop(0)
        high=stack.pop(0)
        if high <= low:
            continue
        pivot = lst[high]
        i = low - 1
        for j in range(low,high+1):
            if lst[j] <= pivot:
                i += 1
                lst[i],lst[j] = lst[j],lst[i]
        stack.extend([low,i-1,i+1,high])
    return lst
        
        
        
        
        
        
        
        