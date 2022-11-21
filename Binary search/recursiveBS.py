#recursive BS
def b_s(arr, low, high, x):
    if high >= low:
        mid = (high + low) //2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return b_s(arr, low, mid-1, x)
        else:
            return b_s(arr, mid + 1, high, x)

    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9, 10]
x = 10
res = b_s(arr, 0, len(arr)-1, x)
if res != -1:
    print('index:', str(res))
else:
    print('is not present in array')