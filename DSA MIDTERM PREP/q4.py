def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]

    i = j = 0
    k = p

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1

def mergesort(A, p, r):
    if p < r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
        print(A[p:r+1])

A = [52, 37, 63, 14, 17, 8, 6, 25]
mergesort(A, 0, len(A)-1)
print("Sorted Array:", A)
