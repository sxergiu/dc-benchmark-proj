import tkinter as tk
import benchmark as bm

# Create the main window
root = tk.Tk()
root.title("Benchmarks of The Unnamed")

# Function to switch the content based on the button clicked
def exit_app():
    print("Exit button clicked")
    root.quit()
def switch_content(content):
    current_content.pack_forget()
    content.pack(fill=tk.BOTH, expand=True)
    globals()['current_content'] = content

# Define default content
default_content = tk.Frame(root)
default_label = tk.Label(default_content, text='Default/Welcome')
default_label.pack(fill=tk.BOTH, expand=True)

# Define different contents for each button
content1 = tk.Frame(root)
label1 = tk.Label(content1, text='Metodele de benchmark folosite/ cum functioneaza scorul')
label1.pack(fill=tk.BOTH, expand=True)

content2 = tk.Frame(root)

def compute_button_func(low_entry, high_entry, size_entry):
    button_compute = tk.Button(content2, text="Compute", command=lambda: bm.compute_commands(low_entry, high_entry, size_entry) )
    button_compute.pack(pady=5)
def run_benchmarks():
    print("Benchmarks button clicked")
    low_label = tk.Label(content2, text="Low value:")
    low_label.pack()
    low_entry = tk.Entry(content2)
    low_entry.pack()

    high_label = tk.Label(content2, text="High value:")
    high_label.pack()
    high_entry = tk.Entry(content2)
    high_entry.pack()

    size_label = tk.Label(content2, text="Size:")
    size_label.pack()
    size_entry = tk.Entry(content2)
    size_entry.pack()
    compute_button_func(low_entry, high_entry, size_entry)


'''
label2 = tk.Label(content2, text='Content for Button 2')
label2.pack(fill=tk.BOTH, expand=True)
button_in_content2 = tk.Button(content2, text='Button in Content 2')
'''

content3 = tk.Frame(root)
label3 = tk.Label(content3, text='Specificatiile curente:')
label3.pack(fill=tk.BOTH, expand=True)

content4 = tk.Frame(root)
label4 = tk.Label(content4, text='Istoric')
label4.pack(fill=tk.BOTH, expand=True)

# Pack default content initially
default_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
current_content = default_content


# Create a frame for button list
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Button 1
button1 = tk.Button(button_frame, text='About the app', command=lambda: switch_content(content1))

# Button 2
button2 = tk.Button(button_frame, text='Benchmarking', command=lambda: [switch_content(content2), run_benchmarks()])

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
