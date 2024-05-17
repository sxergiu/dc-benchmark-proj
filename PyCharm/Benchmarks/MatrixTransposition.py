import numpy as np
import time
import multiprocessing

def transpose_matrix(matrix, result_queue):
    transposed = np.transpose(matrix)
    result_queue.append(transposed)

def transpose_matrix_parallel(array_of_mat):
    result_queue = []
    list_of_processes = []
    count = 0

    for i in range(0, len(array_of_mat)):
        count += 1
        for j in range(0, 2):
            matrix = array_of_mat[i][0][j]
            if count % 2 == 0:
                process = multiprocessing.Process(target=transpose_matrix, args=(matrix, result_queue))
                list_of_processes.append(process)
                process.start()
            else:
                transpose_matrix(matrix, result_queue)
    
    for process in list_of_processes:
        process.join()
    return time.time()

