import numpy as np

""" 2 matrices per file, also 2 multiplied per process  => powers of 2
"""
list_of_tuples_size = (32, 32)    #size
num_pairs = 4          #numbers of tuples
chunk_size = 2         #numbers of matrices multiplied per process


def hasContentFile():
    with open("dc-benchmark-proj\\MatricesDB\\test.txt", "r") as fp:
        first_char = fp.read(1)
        if not first_char:
            return False
        return True
    
def write_in_file(list_of_tuples):
    if hasContentFile() == True:
        with open("dc-benchmark-proj\\MatricesDB\\test.txt", "w") as fp:
            for i in range(0,2):
                matrix = list_of_tuples[0][i]
                for x in range(list_of_tuples_size[0]):  #rows
                    for y in range(list_of_tuples_size[0]):   #columns
                        fp.write(str(matrix[x][y]) + " ")
                    fp.write('\n')
    else:
        with open("dc-benchmark-proj\\MatricesDB\\test.txt", "a+") as fp:
            for i in range(0,2):
                matrix = list_of_tuples[0][i]
                for x in range(list_of_tuples_size[0]):  #rows
                    for y in range(list_of_tuples_size[0]):   #columns
                        fp.write(str(matrix[x][y]) + " ")
                    fp.write('\n')



""" for how many pairs you have
    stores in array_of_mat tuples of 2 matrices of dimension matrix_size
"""
def generate_matrices():   
    array_of_mat = []
    for _ in range(num_pairs): 
        list_of_tuples = [(np.random.rand(*list_of_tuples_size), np.random.rand(*list_of_tuples_size))]
        array_of_mat.append(list_of_tuples)
        write_in_file(list_of_tuples)
    return array_of_mat