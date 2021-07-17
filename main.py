# Importing NumPy Library
import numpy as np

n = 4

A = np.array([[1, 2, 1, -1],[3, 2, 4, 4],[4, 4, 3, 4],[2, 0, 1, 5]])
b = np.array([5,16,22,15])

print("solution of numpy")
print(np.linalg.solve(A,b))

c=np.zeros((n,n))
d=np.zeros((n))

print('A Original: ')
print(A)
print('b Original: ')
print(b)
print(' ')


#foward elimination, upper triangle matrix creation
#k is the diagnals
#i is the rows
#j is the columns
#n is the number of unknowns\answers

for k in range(n): # Loop through the columns of the matrix
    Maximum = abs(A[k, k])
    line = k
    for i in range(k +1, n):   # searching for max row value in the columns
        if abs(A[i, 0]) > Maximum:
            Maximum = abs(A[i, 0])
            line = i
    if line != k:
        #A row changing
        c[k,:] = A[k,:]
        A[k,:] = A[line,:]
        A[line,:] = c[k,:]
        # B row changing
        d[k] = b[k]
        b[k] = b[line]
        b[line] = d[k]
        #A[line], A[k] = (A[k].copy(), A[line].copy())  # taking copy of the first row
        #b[k], b[line] = (b[line], b[k])  # Swapping the rows


    for i in range(k+1 , n):  # creating a triangular matrix
        ws = float(A[i, k] / A[k, k])  # the factor is the same as for the usual Gaussian method
        print("A: \n", A)
        print("b \n", b)
        for j in range(k, n):  # for the next row, elimination, formula from problem 1
            A[i, j] = A[i, j] - float(ws* A[k, j])
            #print("A: \n", A)
            #print("b \n", b)
        b[i] = b[i]- float(ws* b[k])

# Checking the results
print('A: ')
print(A)
print('b: ')
print(b)
print(' ')
print(' ')

#back substitution, to find X values
x = np.zeros(n)
x[n-1] = float(b[n-1]/A[n-1, n-1])
for i in range (n-2, -1, -1):
    sum_j = 0
    for j in range(i+1, n):
        sum_j += float(A[i,j]* x[j])
    x[i] = float((b[i] - sum_j)/A[i,i])

print('The answer for X: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')