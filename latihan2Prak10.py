#Dinda Rahmadanty Alamsyah
#065002500028

def bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return bubble_sort(arr, n - 1)

data = [5, 1, 4, 2, 8]
hasil = bubble_sort(data)
print("Hasil sorting:", hasil)