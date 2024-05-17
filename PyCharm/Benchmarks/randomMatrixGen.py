import numpy as np

""" 2 matrices per file, also 2 multiplied per process  => powers of 2
"""
list_of_tuples_size = (512, 512)    #size
num_pairs = 4         #numbers of tuples
chunk_size = 2         #numbers of matrices multiplied per process


def hasContentFile():
    #with open("dc-benchmark-proj\\MatricesDB\\test.txt", "r") as fp: #for windows
    with open("MatricesDB/test.txt", "r") as fp: #for linux
        first_char = fp.read(1)
        if not first_char:
            return False
        return True
    
def write_in_file(array_of_mat):
    if hasContentFile() == True:
        mode = "w"
    else:
        mode = "a+"

    with open("MatricesDB/test.txt", mode) as fp:
        for list_of_tuples in array_of_mat:
            for tuple in list_of_tuples:
                for matrix in tuple:
                    for row in matrix:
                        for value in row:
                            fp.write(str(value) + " ")
                        fp.write("\n")

""" for how many pairs you have
    stores in array_of_mat tuples of 2 matrices of dimension matrix_size
"""
def generate_matrices():   
    array_of_mat = []
    for _ in range(num_pairs): 
        list_of_tuples = [(np.random.rand(*list_of_tuples_size), np.random.rand(*list_of_tuples_size))]
        array_of_mat.append(list_of_tuples)
    write_in_file(array_of_mat)
    return array_of_mat