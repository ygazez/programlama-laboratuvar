arr=[4, -3, 2, -1, -2, 6, -5]

def maks(arr):
    sayi = 0
    enbuyuk = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sayi += arr[j]
            if(sayi>enbuyuk):
                enbuyuk = sayi
        sayi = 0
    return enbuyuk
print(max_sum(arr))
