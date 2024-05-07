import tkinter as tk
import randomMatrixGen as matGen
import os
from MatrixMultiplicationBenchmark import myFunc


def open_settings():
    print("Settings button clicked")

def exit_app():
    print("Exit button clicked")
    root.quit()
    

def run_benchmarks():
    print("Benchmarks button clicked")


root = tk.Tk()
root.title("Benchmarks of The Unnamed")

button_benchmarks = tk.Button(root, text="Benchmarks", command=run_benchmarks)
button_benchmarks.pack(pady=5)

button_settings = tk.Button(root, text="Settings", command=open_settings)
button_settings.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_app)
button_exit.pack(pady=5)

root.mainloop()
