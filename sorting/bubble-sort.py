def bub(A):
    x = len(A) - 1
    for i in range(x):
        for j in range(x-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

A = input('Enter the list values to be stored: ').split()
bub(A)
print(A)
