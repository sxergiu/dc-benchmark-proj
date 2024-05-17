import ComputeMatrixMultiplication as compMat
import digitsOfPi as pi
import tkinter as tk
import sysInfo as cs
import threading
import ramRWSpeed as rw


specs = cs.getSpecs()

# Create the main window
root = tk.Tk()
root.title("Benchmarks of The Unnamed")

# Function to switch the content based on the button clicked
def switch_content(content):
    current_content.pack_forget()
    content.pack(fill=tk.BOTH, expand=True)
    globals()['current_content'] = content

# Define default content
default_content = tk.Frame(root)
default_label = tk.Label(default_content, text='Welcome to The Unnamed Benchmark! We are a team of Arabians, proud that we can introduce you to our app.')
default_label.pack(fill=tk.BOTH, expand=True)

# Content 1 - About the App
content1 = tk.Frame(root)
label1 = tk.Label(content1, text='Metodele de benchmark folosite/ cum functioneaza scorul')
label1.pack(fill=tk.BOTH, expand=True)

# Content 2 - Benchmarking

def compute_pi():
    try:
        digits = int(digits_entry.get())
        if digits <= 0:
            raise ValueError("Number of digits must be a positive integer.")

        time_taken = pi.benchmark_pi(digits)  # Call the function from the imported module
        resultPI_label.config(text=f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")
    except ValueError as e:
        resultPI_label.config(text=str(e))

def compute_matrix_multip():
    resultMat_label.config(text="Computing matrix operations...")
    thread = threading.Thread(target=mat_wrapper)  # Use a thread to run mat() function
    thread.start()

def mat_wrapper():
    compMat.mat()
    resultMat_label.config(text="Matrix operations completed.")


def compute_rw():
    try:
        digits = int(mb_entry.get())
        if digits <= 0:
            raise ValueError("Number of MB must be a positive integer.")

        speed = rw.memory_read_write_speed_test()
        resultRW_label.config(text=speed)
        
    except ValueError as e:
        resultRW_label.config(text=str(e))

"""def compute_matrix_multip():
    compMat.mat()
"""
content2 = tk.Frame(root)

digits_label = tk.Label(content2, text="Enter the number of digits of Pi to calculate:")
digits_label.pack()

digits_entry = tk.Entry(content2)
digits_entry.pack()

compute_pi_button = tk.Button(content2, text="Compute Pi", command=compute_pi)
compute_pi_button.pack()

resultPI_label = tk.Label(content2, text="")
resultPI_label.pack()

compute_matrix_multip_button = tk.Button(content2, text="Compute Matrix", command=compute_matrix_multip)
compute_matrix_multip_button.pack()

resultMat_label = tk.Label(content2, text="")
resultMat_label.pack()

mb_label = tk.Label(content2, text="Enter the number of MB to benchmark:")
mb_label.pack()

mb_entry = tk.Entry(content2)
mb_entry.pack()

compute_speed_button = tk.Button(content2, text="Read/Write speed", command=compute_rw)
compute_speed_button.pack()

resultRW_label = tk.Label(content2, text="")
resultRW_label.pack()


# Content 3 - Computer Specs
content3 = tk.Frame(root)
label3 = tk.Label(content3, text='Current Specs: \n' + str(specs))
label3.pack(fill=tk.BOTH, expand=True)

# Content 4 - History
content4 = tk.Frame(root)
label4 = tk.Label(content4, text='Istoric')
label4.pack(fill=tk.BOTH, expand=True)

def exit_app():
    print("Exit button clicked")
    root.quit()

# Pack default content initially
default_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
current_content = default_content

# Create a frame for button list
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Button 1
button1 = tk.Button(button_frame, text='About the app', command=lambda: switch_content(content1))

# Button 2
button2 = tk.Button(button_frame, text='Benchmarking', command=lambda: switch_content(content2))

# Button 3
button3 = tk.Button(button_frame, text='Computer Information', command=lambda: switch_content(content3))

# Button 4
button4 = tk.Button(button_frame, text='History', command=lambda: switch_content(content4))

# Exit Button
button5 = tk.Button(button_frame, text="Exit", command=exit_app)

button_list = [button1, button2, button3, button4, button5]

# Pack buttons
for button in button_list:
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
