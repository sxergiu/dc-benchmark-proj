from randomMatrixGen import *

    
def compute_dot_product(array_of_mat):
    start = time.time()
    
    middle = len(array_of_mat) // 2     #integer division

    for firstHalf in array_of_mat[:middle]:
        for secondHalf in array_of_mat[middle:]:
            np.dot(firstHalf, secondHalf)
    end = time.time()

    return abs(end - start)
    

"""print("MATRIX GENERATION\n")
print("Enter ranges of values in matrices: \n")
low_range = int(input("Low value: "))
high_range = int(input("High value: "))
size = int(input("Enter how many matrices to generate: "))

start = time.time()

array_of_mat = generate_matrices(low_range, high_range, size)
compute_dot_product(array_of_mat)

end = time.time()
print(str(abs(end - start)))
"""
