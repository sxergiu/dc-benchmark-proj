import numpy as np
import time
import multiprocessing
import randomMatrixGen as matrixGen


""" takes from array_of_mat tuples from current index to i + chunk_size - 1
    and stores them inside an array of matrices which is matrix_chunk
    matrix_chunk is a list containg 1 element which is a sublist
"""
def generate_chunks(array_of_mat):
    for i in range(0, len(array_of_mat), matrixGen.chunk_size):
        matrix_chunk = [array_of_mat[i:i+matrixGen.chunk_size]]
        print("This is a matrix chunk: " + '\n' + str(matrix_chunk) + '\n')    
        store_processes(matrix_chunk)                       

""" create a queue to store each result from multiplication
    create a list of processes to store processes
    each process has as target compute_dot_product(chunk, result_queue)
    at the end wait for all processes to finish
"""
def store_processes(matrix_chunk):
    result_queue = multiprocessing.Queue()
    list_of_processes = []

    for chunk in matrix_chunk:
        print("This is a chunk: " + '\n' + str(chunk) + '\n')  
        process = multiprocessing.Process(target=compute_dot_product, args=(chunk, result_queue))
        list_of_processes.append(process)
        process.start()

    for process in list_of_processes:
        process.join() #wait for process

""" when you call the function with chunk argument you give it a tuple of 2 matrices
    it multiplies them and store the result matrix in a list of matrices
    then
"""
def compute_dot_product(chunk, result_queue):
    results = []
        #print("This is a matrix pair: " + '\n' + str(matrix_pair) + '\n')  
    result = np.dot(chunk[0], chunk[1])
    results.append(result)

    result_queue.put(results)
    

def main():
    array_of_mat = matrixGen.generate_matrices()
    start = time.time()
    generate_chunks(array_of_mat)
    end = time.time()
    print("Time is: " + str(abs(end - start)))

if __name__ == "__main__":
    main()