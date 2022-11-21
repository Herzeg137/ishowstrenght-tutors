#iterative method in Binary Search.
def b_s(arr, x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (low+high)//2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 5

res = b_s(arr, x)
if res != -1:
    print('index: ', res)
else:
    print('is not present in arr')

#Bu dastur. faqat berilgan qiymatni nechanchi index da ekanligini O(log n) bilan topadi. index() funksiyasidan tez.
#Agar index() funksiyasini ishlatsak uning TC si bunday: O(N*log(n)) bu linear search ya'ni O(n) dan astaroq.
#Binary search: O(log n)
#O(log n) > O(N*log n)