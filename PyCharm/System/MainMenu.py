import tkinter as tk
import sys
sys.path.append("..")
from Benchmarks.Pi import digitsOfPi as pi
from System import benchmark as bm
from System import sysInfo as cs

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
default_label = tk.Label(default_content, text='Welcome to The Unnamed Benchmark! Currently the following benchmarks are available: Digits of Pi, cristi nush cum fac cu matricile alea')
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
        result_label.config(text=f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")
    except ValueError as e:
        result_label.config(text=str(e))

def compute_matrix_multip(low_entry, high_entry, size_entry):
    button_compute = tk.Button(content2, text="Compute", command=lambda: bm.compute_commands(low_entry, high_entry, size_entry) )
    button_compute.pack(pady=5)

content2 = tk.Frame(root)

digits_label = tk.Label(content2, text="Enter the number of digits of Pi to calculate:")
digits_label.pack()

digits_entry = tk.Entry(content2)
digits_entry.pack()

result_label = tk.Label(content2, text="")
result_label.pack()

compute_pi_button = tk.Button(content2, text="Compute", command=compute_pi)
compute_pi_button.pack()

# compute_matrix_multip_button = tk.Button(content2, text="Compute Matrix", command=compute_matrix_multip(0,0,0))
# compute_matrix_multip_button.pack()

''' populating content example
label2 = tk.Label(content2, text='Content for Button 2')
label2.pack(fill=tk.BOTH, expand=True)
button_in_content2 = tk.Button(content2, text='Button in Content 2')
'''

#Content 3 - Computer Specs
content3 = tk.Frame(root)
label3 = tk.Label(content3, text='Current Specs: ' + str(specs))
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
button5 = tk.Button(button_frame, text="Exit", command=lambda: exit_app())

button_list = [button1, button2, button3, button4, button5]

# Pack buttons
for button in button_list:
    button.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

root.mainloop()
