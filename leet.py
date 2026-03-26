def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))