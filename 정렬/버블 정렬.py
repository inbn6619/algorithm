# O(n**2)

array = [8,4,6,2,9,1,3,7,5]

def bubble_sort(array):
    n = len(array)

    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

bubble_sort(array)