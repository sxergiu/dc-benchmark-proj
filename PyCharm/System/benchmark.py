import tkinter as tk
import PyCharm.Benchmarks.MatMult as matMult

def create_result(result):
    result_panel = tk.Tk()
    result_panel.title("Time")

    result_label = tk.Label(result_panel, text=str(result))
    result_label.pack()
    result_panel.mainloop()

def compute_commands(low_entry, high_entry, size_entry):
    low = int(low_entry.get())
    high = int(high_entry.get())
    size = int(size_entry.get())

    array_of_mat = matMult.generate_matrices(low, high, size)
    res = matMult.compute_dot_product(array_of_mat)
    create_result(res)

