import numpy as np
import time


def write_in_file(matrix):
    fp = open("matrixDB.txt", "a")
    for row in matrix:
        row_str = ' '.join(map(str, row))
        fp.write(row_str + '\n')
    fp.close()

def generate_matrices(low_range, high_range, number_of_mat):
    array_of_mat = []
    for i in range(0, number_of_mat):
        array_of_mat.append(np.random.randint(low_range, high_range, size=(1000, 1000)))
        write_in_file(array_of_mat[i])
    return array_of_mat