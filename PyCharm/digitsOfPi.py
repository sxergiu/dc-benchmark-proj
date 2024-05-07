import time
import mpmath

def benchmark_pi(digits):
    start_time = time.time()
    with mpmath.workdps(digits):
        _ = str(mpmath.pi)  # Calculating Pi but not storing it
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    digits = int(input("Enter the number of digits of Pi to calculate: "))
    time_taken = benchmark_pi(digits)
    print(f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")

# Functia benchmark_pi() returneaza timpul de calcul, aici schimbi variabila digits ca sa calculeze pt diferite lungimi si aiae