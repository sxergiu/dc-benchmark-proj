import tkinter as tk
import ComputeMatrixMultiplication as matMult


def open_settings():
    print("Settings button clicked")

def exit_app():
    print("Exit button clicked")
    root.quit()

def create_result(result):

    result_panel = tk.Tk()
    result_panel.title("Time")
    
    result_label = tk.Label(result_panel, text=str(result))
    result_label.pack()
    result_panel.mainloop()

def compute_commands(low_entry, high_entry, size_entry):
    low = int(low_entry.get())
    high = int(high_entry.get())
    size = int (size_entry.get())

    array_of_mat = matMult.generate_matrices(low, high, size)
    res = matMult.compute_dot_product(array_of_mat)
    create_result(res)

    root.quit()

def compute_button_func(low_entry, high_entry, size_entry):
    button_compute = tk.Button(root, text="Compute", command=lambda: compute_commands(low_entry, high_entry, size_entry))
    button_compute.pack(pady=5)

def run_benchmarks():
    print("Benchmarks button clicked")
    low_label = tk.Label(root, text="Low value:")
    low_label.pack()
    low_entry = tk.Entry(root)
    low_entry.pack()

    high_label = tk.Label(root, text="High value:")
    high_label.pack()
    high_entry = tk.Entry(root)
    high_entry.pack()

    size_label = tk.Label(root, text="Size:")
    size_label.pack()
    size_entry = tk.Entry(root)
    size_entry.pack()

    compute_button_func(low_entry, high_entry, size_entry)

root = tk.Tk()
root.title("Benchmarks of The Unnamed")


#create buttons
button_benchmarks = tk.Button(root, text="Benchmarks", command=run_benchmarks)
button_benchmarks.pack(pady=5)

button_settings = tk.Button(root, text="Settings", command=open_settings)
button_settings.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_app)
button_exit.pack(pady=5)

root.mainloop()
