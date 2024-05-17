import tkinter as tk
import threading
import ComputeMatrixMultiplication as compMat
import digitsOfPi as pi
import sysInfo as cs
import ramRWSpeed as rw

specs = cs.getSpecs()

# Create the main window
root = tk.Tk()
root.title("Benchmarks of The Unnamed")
root.geometry("800x600")  # Set a fixed window size for better control

# Function to switch the content based on the button clicked
def switch_content(content):
    current_content.pack_forget()
    content.pack(fill=tk.BOTH, expand=True)
    globals()['current_content'] = content

# Define default content
default_content = tk.Frame(root)
default_label = tk.Label(default_content, text='"The Unnamed Benchmark" is a comprehensive application developed by a group of students\n aimed at benchmarking computer system\'s RAM and CPU performance.\n The application employs various computational tasks to evaluate system capabilities,\n including matrix multiplication, inversions, and transpositions,\nalong with sequential and random reading and writing operations.\n Additionally, the application incorporates computations involving\n digits of pi to further stress test the system\'s processing capabilities. \nBy executing these tasks, users can gain insights into their system\'s performance under different\ncomputational workloads, aiding in system optimization and performance tuning.')
default_label.pack(fill=tk.BOTH, expand=True)

# Content 1 - About the App
content1 = tk.Frame(root)
label1 = tk.Label(content1, text='Metodele de benchmark folosite/ cum functioneaza scorul')
label1.pack(fill=tk.BOTH, expand=True)

# Content 2 - Benchmarking

# Function to compute Pi
def compute_pi():
    try:
        digits = int(digits_entry.get())
        if digits <= 0:
            raise ValueError("Number of digits must be a positive integer.")
        time_taken = pi.benchmark_pi(digits)  # Call the function from the imported module
        resultPI_label.config(text=f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")
    except ValueError as e:
        resultPI_label.config(text=str(e))

def compute_pi_powers():
    try:
        digits = int(digits_entry.get())
        if digits <= 0:
            raise ValueError("Number of digits must be a positive integer.")
        pi.powers_of_pi(digits)
    except ValueError as e:
        resultPI_label.config(text=str(e))

# Function to compute Matrix Multiplication
def compute_matrix_multip():
    resultMat_label.config(text="Computing matrix operations...")
    display_pi_button.config(state=tk.DISABLED)
    display_rw_button.config(state=tk.DISABLED)
    thread = threading.Thread(target=mat_wrapper)  # Use a thread to run mat() function
    thread.start()

def mat_wrapper():
    compMat.mat()
    resultMat_label.config(text="Matrix operations completed.")
    display_pi_button.config(state=tk.NORMAL)
    display_rw_button.config(state=tk.NORMAL)

# Function to compute Read/Write Speed
def compute_rw():
    try:
        mb = int(mb_entry.get())
        if mb <= 0:
            raise ValueError("Number of MB must be a positive integer.")
        speed = rw.memory_read_write_speed_test()
        resultRW_label.config(text=rw.res_to_string(speed))
    except ValueError as e:
        resultRW_label.config(text=str(e))

# Function to show Pi section
def show_pi_section():
    display_pi_button.pack_forget()
    pi_section.place(x=370, y=300)
    display_rw_button.config(state=tk.DISABLED)
    compute_matrix_multip_button.config(state=tk.DISABLED)

# Function to hide Pi section
def hide_pi_section():
    pi_section.place_forget()
    display_pi_button.pack()
    display_rw_button.config(state=tk.NORMAL)
    compute_matrix_multip_button.config(state=tk.NORMAL)

# Function to show Read/Write Speed section
def show_rw_section():
    display_rw_button.pack_forget()
    rw_section.place(x=370, y=300)
    display_pi_button.config(state=tk.DISABLED)
    compute_matrix_multip_button.config(state=tk.DISABLED)

# Function to hide Read/Write Speed section
def hide_rw_section():
    rw_section.place_forget()
    display_rw_button.pack()
    display_pi_button.config(state=tk.NORMAL)
    compute_matrix_multip_button.config(state=tk.NORMAL)

content2 = tk.Frame(root)

# Benchmark buttons frame
benchmark_buttons_frame = tk.Frame(content2)
benchmark_buttons_frame.pack()

# Matrix Multiplication section
compute_matrix_multip_button = tk.Button(benchmark_buttons_frame, text="Compute Matrix Multiplication", command=compute_matrix_multip)
compute_matrix_multip_button.pack()

resultMat_label = tk.Label(content2, text="")
resultMat_label.pack()

# Button to display Pi section
display_pi_button = tk.Button(benchmark_buttons_frame, text="Pi", command=show_pi_section)
display_pi_button.pack()

# Pi section
pi_section = tk.Frame(root)

digits_label = tk.Label(pi_section, text="Enter the number of digits of Pi to calculate:")
digits_label.pack()

digits_entry = tk.Entry(pi_section)
digits_entry.pack()

compute_pi_button = tk.Button(pi_section, text="Compute Pi", command=compute_pi)
compute_pi_button.pack()

compute_pi_button2 = tk.Button(pi_section, text="Plot Powers of Pi", command=compute_pi_powers)
compute_pi_button2.pack()

resultPI_label = tk.Label(pi_section, text="")
resultPI_label.pack()

cancel_pi_button = tk.Button(pi_section, text="Cancel", command=hide_pi_section)
cancel_pi_button.pack()

# Button to display Read/Write Speed section
display_rw_button = tk.Button(benchmark_buttons_frame, text="Read/Write Speed", command=show_rw_section)
display_rw_button.pack()

# Read/Write Speed section
rw_section = tk.Frame(root)

mb_label = tk.Label(rw_section, text="Enter the number of MB to benchmark:")
mb_label.pack()

mb_entry = tk.Entry(rw_section)
mb_entry.pack()

compute_speed_button = tk.Button(rw_section, text="Compute Read/Write Speed", command=compute_rw)
compute_speed_button.pack()

resultRW_label = tk.Label(rw_section, text="")
resultRW_label.pack()

cancel_rw_button = tk.Button(rw_section, text="Cancel", command=hide_rw_section)
cancel_rw_button.pack()

# Content 3 - Computer Specs
content3 = tk.Frame(root)
label3 = tk.Label(content3, text='Current Specs: \n' + str(specs))
label3.pack(fill=tk.BOTH, expand=True)

# Content 4 - History
content4 = tk.Frame(root)
label4 = tk.Label(content4, text='Istoric')
label4.pack(fill=tk.BOTH, expand=True)

# Function to exit the application
def exit_app():
    print("Exit button clicked")
    root.quit()

# Pack default content initially
default_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
current_content = default_content

# Create a frame for button list
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Buttons for navigation
button1 = tk.Button(button_frame, text='About the app', command=lambda: switch_content(content1))
button2 = tk.Button(button_frame, text='Benchmarking', command=lambda: switch_content(content2))
button3 = tk.Button(button_frame, text='Computer Information', command=lambda: switch_content(content3))
button4 = tk.Button(button_frame, text='History', command=lambda: switch_content(content4))
button5 = tk.Button(button_frame, text="Exit", command=exit_app)

button_list = [button1, button2, button3, button4, button5]

# Pack buttons
for button in button_list:
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
