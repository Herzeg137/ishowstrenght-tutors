#iterative method in Binary Search.
#qadamlarni sanaydi. Nechta amal bajarganini sanaydi. va uni chiqaradi.
def b_s(arr, x, steps = 0):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid + 1
            steps += 1
        elif arr[mid] > x:
            high = mid - 1
            steps += 1
        else:
            print(f'steps: {steps}')
            return mid

    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 10

res = b_s(arr, x, steps = 0)
if res != -1:
    print('index: ', res)
else:
    print('is not present in arr')
