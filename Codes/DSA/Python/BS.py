def BinarySearch(target,elements):
    s = 0
    e = len(elements) - 1
    while s<=e:
        m = (s + e)//2
        if elements[m] == target:
            return m
        elif elements[m]<target:
            s = m + 1
        else:
            e = m - 1
    
    return -1

elements = [7 , 8 , 9 , 10 , 12]
target = 7
index = BinarySearch(target,elements)

if index<0:
    print("Element not found")
else:
    print(index)