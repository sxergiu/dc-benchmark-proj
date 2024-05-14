import randomMatrixGen as matGen
import numpy as np
import time

def transposeMatrix(array_of_mat):
    for i in range(0, len(array_of_mat)):
        for j in range(0, 2):
            matrix = array_of_mat[i][0][j]
            transposed = np.transpose(matrix)


array_of_mat = matGen.generate_matrices()
start = time.time()
transposeMatrix(array_of_mat)
end = time.time()
print(str(abs(end - start)))