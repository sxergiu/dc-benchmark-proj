import numpy as np
import time

"""
start = time.time()
matrix1 = np.random.randint(1000000,10000000, size=(1000,1000))
matrix2 = np.random.randint(1000000,10000000, size=(1000,1000))

print(str(matrix1 * matrix2))
end = time.time()

print("Time for np is: " + str(end - start))

"""
matA = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(1000000)
    matA.append(row)

matB = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(1000000)
    matB.append(row)
start1 = time.time()


# Initialize the resulting matrix with zeros
result = [ [0 for _ in range(1000)] for _ in range(1000) ]

# Matrix multiplication
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            result[i][j] += matA[i][k] * matB[k][j]


print(result)
end1 = time.time()
print("Time for normal mat is: " + str(end1 - start1))
