import numpy as np
import time
import random
import matplotlib.pyplot as plt

size_mb = 100

def memory_read_write_speed_test(mb):

    size_mb = mb
    size = size_mb * 1024 * 1024 // 8  # Convert MB to number of 8-byte doubles
    array = np.zeros(size, dtype=np.float64)

    # Sequential Write
    start_time = time.time()
    for i in range(size):
        array[i] = i
    sequential_write_time = time.time() - start_time

    # Sequential Read
    start_time = time.time()
    for i in range(size):
        temp = array[i]
    sequential_read_time = time.time() - start_time

    # Random Write
    start_time = time.time()
    for i in range(size):
        index = random.randint(0, size - 1)
        array[index] = i
    random_write_time = time.time() - start_time

    # Random Read
    start_time = time.time()
    for i in range(size):
        index = random.randint(0, size - 1)
        temp = array[index]
    random_read_time = time.time() - start_time

    results = {
        "Sequential Write": sequential_write_time,
        "Sequential Read": sequential_read_time,
        "Random Write": random_write_time,
        "Random Read": random_read_time
    }

    return results

def res_to_string(results):
    formatted_results = ""
    for key, value in results.items():
        formatted_results += f"{key}: {value}\n"
    return formatted_results

if __name__ == "__main__":
    results = memory_read_write_speed_test()
