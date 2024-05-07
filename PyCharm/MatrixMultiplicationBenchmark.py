import os
import numpy as np
import time
import multiprocessing as mp    

directory = "./MatricesDB/"

def traverse_dirs():
    array_of_mat = []
    for name in os.listdir(directory):
        file_path = os.path.join(directory, name)
        if os.path.isfile(file_path):
            matrix = []
            with open(file_path, 'r') as file:
                for line in file:
                    row = list(map(float, line.strip().split()))
                    matrix.append(row)
            array_of_mat.append(matrix)

    print("Number of matrices:", len(array_of_mat))
    compute_dot_product(array_of_mat)

def compute_dot_product(array_of_mat):
    start = time.time()
    middle = len(array_of_mat) // 2  # Integer division

    for firstHalf in array_of_mat[:middle]:
        for secondHalf in array_of_mat[middle:]:
            np.dot(firstHalf, secondHalf)
    end = time.time()

    print("Time taken:", abs(end - start))


