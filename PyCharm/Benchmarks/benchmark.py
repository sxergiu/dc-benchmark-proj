import numpy as np
import time
import multiprocessing
import randomMatrixGen as matrixGen
import MatrixInversion
import MatrixTransposition
import matplotlib.pyplot as plt
from ComputeMatrixMultiplication import generate_chunks


number_of_tests = 2

def mat():
    times = []
    cnt = 0
    sum = 0

    array_of_mat = matrixGen.generate_matrices()
    for _ in range(number_of_tests):
        start = time.perf_counter()
        generate_chunks(array_of_mat)
        MatrixInversion.inverse_matrix_parallel(array_of_mat)
        MatrixTransposition.transpose_matrix_parallel(array_of_mat)
        end = time.perf_counter()
        cnt += 1
        sum += end - start
        times.append(end - start)
    print("Time spent: ", sum)
    print("Average time is: ", sum / cnt)

    x_axis = []
    y_axis = []
    for x_value in range(1, number_of_tests + 1):
        x_axis.append(x_value)
    for y_value in times:
        y_axis.append(y_value)
    
    plt.plot(x_axis, y_axis)
    plt.xlabel("x axix")
    plt.ylabel("y axis")
    plt.title("Matrix operations results")
    plt.show()

if __name__ == "__main__":
    #multiprocessing.freeze_support()
    mat()
