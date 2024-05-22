import numpy as np
import ComputeMatrixMultiplication as compMat
import digitsOfPi as compPi
from ramRWSpeed import memory_read_write_speed_test as ramTest
def score():
    digits = 1000  # digits of pi

    mat_op_times = compMat.mat()
    pi_op_times, time_for_pi_digits = compPi.powers_of_pi(digits)
    _, ram_times = ramTest(100)

    max_mat_time = max(mat_op_times)
    max_pi_time = max(pi_op_times)
    max_ram_time = max(ram_times)
    
    normalized_mat_times = [time / max_mat_time for time in mat_op_times]
    normalized_pi_times = [time / max_pi_time for time in pi_op_times]
    normalized_ram_times = [time / max_ram_time for time in ram_times]

    normalized_avg_mat = sum(normalized_mat_times) / len(normalized_mat_times)
    normalized_avg_pi = sum(normalized_pi_times) / len(normalized_pi_times)
    normalized_avg_ram = sum(normalized_ram_times) / len(normalized_ram_times)

    total_score = normalized_avg_mat * 0.4 + normalized_avg_pi * 0.2 + time_for_pi_digits * 0.1 + normalized_avg_ram * 0.3

    print("Score(t): ", total_score * 100)
    return total_score*100

if __name__ == "__main__":
    score()
