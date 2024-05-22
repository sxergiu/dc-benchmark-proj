import time
import mpmath

start_benchmark = 1000
start_benchmark = int(start_benchmark)
repeat_benchmark = 10
repeat_benchmark = int(10)

def benchmark_pi(digits):
    start_time = time.time()
    with mpmath.workdps(digits):
        _ = str(mpmath.pi)  # Calculating Pi but not storing it
    end_time = time.time()
    return end_time - start_time

def get_pi(digits):
    t1 = time.perf_counter()
    mpmath.mp.dps = digits
    pi_value = str(mpmath.mp.pi)
    t2 = time.perf_counter()
    return pi_value, t2 - t1

def powers_of_pi(digits):
    pi, time_for_pi_digits = get_pi(digits)
    pi = float(pi)
    average = 0
    times = []

    for i in range(0, repeat_benchmark):
        start = time.perf_counter()
        for _ in range(0,start_benchmark):
            for x in range(1,1000):
                pi * 2**x
            for x in range(1,10000):
                float(x) / pi
            for x in range(1,10000):
                float(pi) / x
            
        end = time.perf_counter()
        duration = (end - start)
        duration = round(duration, 3)
        times.append(duration)
        average += duration
        print('Time: ' + str(duration) + 's')
    average = round(average / repeat_benchmark, 3)
    print('Average (from {} repeats): {}s'.format(repeat_benchmark, average))
    return times, time_for_pi_digits

    
if __name__ == "__main__":
    digits = int(input("Enter the number of digits of Pi to calculate: "))
    #time_taken = benchmark_pi(digits)
    #print(f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")
    powers_of_pi(digits)