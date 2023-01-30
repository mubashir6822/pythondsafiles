def bubblesort(N):
    n = len(N)
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if N[i] > N[i+1]:
                temp = N[i]
                N[i] = N[i+1]
                N[i+1] = temp


N = [3, 5, 8, 9, 6, 2]
print('Original Array:',N)
bubblesort(N)
print('Sorted Array:',N)
