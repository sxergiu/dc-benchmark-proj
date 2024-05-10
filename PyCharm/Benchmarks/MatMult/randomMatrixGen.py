import numpy as np

""" 2 matrices per file, also 2 multiplied per process  => powers of 2
"""
matrix_size = (50, 50)    #size
num_pairs = 4          #numbers of tuples
chunk_size = 2         #numbers of matrices multiplied per process


def write_in_file(matrix):
    with open("MatricesDB/test.txt", "a") as fp:
        for row in matrix:
            for num in row:
                fp.write(str(num) + ' ')
            fp.write('\n')
        fp.write('\n')  # Add a newline between matrices



""" for how many pairs you have
    stores in array_of_mat tuples of 2 matrices of dimension matrix_size
"""
def generate_matrices():   
    array_of_mat = []
    for _ in range(num_pairs): 
        matrix = [(np.random.rand(*matrix_size), np.random.rand(*matrix_size))]
        array_of_mat.append(matrix)
        write_in_file(matrix)
    print("This is array of mat: " + '\n' + str(array_of_mat) + '\n')
    return array_of_mat