import randomMatrixGen as matGen
import numpy as np
import time
import multiprocessing


def inverse_matrix(matrix, result_queue):
    inverse = np.linalg.inv(matrix)
    result_queue.append(inverse)

def inverse_matrix_parallel(array_of_mat):
    result_queue = []
    list_of_processes = []

    for i in range(0, len(array_of_mat)):
        for j in range(0,2):
            matrix = array_of_mat[i][0][j]
            process = multiprocessing.Process(target=inverse_matrix, args=(matrix, result_queue))
            list_of_processes.append(process)
            process.start()
    
    for process in list_of_processes:
        process.join()
    return time.time()
