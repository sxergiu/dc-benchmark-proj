import numpy as np
import ComputeMatrixMultiplication as compMat
import digitsOfPi as compPi

def score():
    digits = 1000  # digits of pi

    mat_op_times = compMat.mat()
    pi_op_times, time_for_pi_digits = compPi.powers_of_pi(digits)
    
    max_mat_time = max(mat_op_times)
    max_pi_time = max(pi_op_times)
    
    normalized_mat_times = [time / max_mat_time for time in mat_op_times]
    normalized_pi_times = [time / max_pi_time for time in pi_op_times]
    
    normalized_avg_mat = sum(normalized_mat_times) / len(normalized_mat_times)
    normalized_avg_pi = sum(normalized_pi_times) / len(normalized_pi_times)
    
    total_score = normalized_avg_mat * 0.6 + normalized_avg_pi * 0.3 + time_for_pi_digits * 0.1

    print("Score(t) ", total_score * 100)
    return total_score*100

if __name__ == "__main__":
    score()
