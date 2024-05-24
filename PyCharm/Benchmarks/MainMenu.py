import tkinter as tk
from tkinter import ttk
import threading
import Score as sc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import displayHistory as hs
import ComputeMatrixMultiplication as compMat
import digitsOfPi as pi
import sysInfo as cs
import ramRWSpeed as rw
import plotting as plot
from PIL import Image, ImageTk


image = Image.open("PyCharm/Benchmarks/islam.png")
image = image.resize((1250, 900))  # Use Image.LANCZOS for high-quality resizing

specsString, specsInfo = cs.get_system_info()

button_font = ("Lucida Console", 12)
text_font = ("Tahoma", 16)

# Hover effects
def on_enter(e):
    e.widget['background'] = '#a0a0a0'

def on_leave(e):
    e.widget['background'] = '#d0d0d0'

# Create the main window
root = tk.Tk()
root.title("Benchmarks of The Unnamed")
root.geometry("1200x800")  # Set a fixed window size for better control
root.configure(bg="#B6B2B9")
bg_image = ImageTk.PhotoImage(image)

# Function to switch the content based on the button clicked
def switch_content(content):
    current_content.pack_forget()
    content.pack(fill=tk.BOTH, expand=True)
    globals()['current_content'] = content
    if content == content4:
        updateHistory()

# Define default content
default_content = tk.Frame(root)

background_label = tk.Label(default_content, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Content 1 - About the App
content1 = tk.Frame(root, bg="#9300FF", bd=100, relief="groove")

about = ("The Unnamed Benchmark\nBenchmarking app for the CPU and RAM memory\nUsing Matrix Multiplication in parallel processes,\nMatrix Inversion,Transposition\nDigits and powers of Pi computation\nRandom and Sequential reading and writing\nSee your current specs and get a score!\nCompare them with others in history!\nAnd don't forget... Lower is better!\n")

label1 = tk.Label(content1, text=about, font=("Lucida Console",18), bg='#9300FF')
label1.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Content 2 - Benchmarking

# Function to compute Pi
def compute_pi():
    try:
        digits = int(digits_entry.get())
        if digits <= 0:
            raise ValueError("Number of digits must be a positive integer.")
        time_taken = pi.benchmark_pi(digits)
        resultPI_label.config(text=f"Time taken to calculate Pi with {digits} digits: {time_taken} seconds")
    except ValueError as e:
        resultPI_label.config(text=str(e))

def compute_pi_powers():
    try:
        digits = int(digits_entry.get())
        if digits <= 0:
            raise ValueError("Number of digits must be a positive integer.")
        times = pi.powers_of_pi(digits)
        fig = plot.plotPi(times)
        display_plot(fig)
    except ValueError as e:
        resultPI_label.config(text=str(e))


# Function to compute Matrix Multiplication

times = None
def compute_matrix_multip():

    thread = threading.Thread(target=mat_wrapper)  # Use a thread to run mat() function
    thread.start()

    thread.join()

    if times is not None:
        fig = plot.plotMat(times, compMat.number_of_tests)
        resultMat_label.config(text="Matrix operations completed.")
        root.after(0, display_plot, fig)

        resultMat_label.after(10000,matLabel())

        display_pi_button.config(state=tk.NORMAL)
        display_rw_button.config(state=tk.NORMAL)
    else:
        resultMat_label.config(text="Matrix operations FAILURE.")

def mat_wrapper():
    global times
    times = compMat.mat()
    

def remove_canvas(widget):
    widget.pack_forget()


def hide_frame(frame, time_ms):
    frame.pack_forget()
    frame.after(time_ms, lambda: frame.pack(fill=tk.BOTH, expand=True))

def display_plot(fig):
    canvas = FigureCanvasTkAgg(fig, master=content2)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.after(15000, remove_canvas, canvas_widget)


# Function to compute Read/Write Speed
def compute_rw():
    try:
        mb = int(mb_entry.get())
        if mb <= 0:
            raise ValueError("Number of MB must be a positive integer.")
        speed,_ = rw.memory_read_write_speed_test(mb)
        fig = plot.plotRW(speed)
        display_plot(fig)
        resultRW_label.config(text=rw.res_to_string(speed))
    except ValueError as e:
        resultRW_label.config(text=str(e))

# Function to show Pi section
def show_pi_section():
    display_pi_button.pack_forget()
    pi_section.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
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
    rw_section.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    display_pi_button.config(state=tk.DISABLED)
    compute_matrix_multip_button.config(state=tk.DISABLED)

# Function to hide Read/Write Speed section
def hide_rw_section():
    rw_section.place_forget()
    display_rw_button.pack()
    display_pi_button.config(state=tk.NORMAL)
    compute_matrix_multip_button.config(state=tk.NORMAL)

def compute_score():
    score = sc.score()
    specsInfo.append(score)
    cs.write_in_file(specsInfo)

content2 = tk.Frame(root, bg="#9300FF", bd=2, relief="groove")

# Frame for Compute Performance label and Run Benchmark button
compute_run_frame = tk.Frame(content2, bg="#9300FF",bd=20, relief="groove")
compute_run_frame.pack(fill=tk.X, padx=20, pady=20)

# Compute Performance label
compute_performance_label = tk.Label(compute_run_frame, text="Compute Performance", font=text_font, bg="#9300FF", bd=15, relief="groove")
compute_performance_label.pack(side=tk.LEFT)

# Run Benchmark button
run_benchmark_button = tk.Button(compute_run_frame, text="Run The Unnamed Benchmark", command=compute_score,
                                    bg="#d0d0d0", font=button_font, bd=5)
run_benchmark_button.pack(side=tk.RIGHT)

# Benchmark buttons frame

background_label = tk.Label(default_content, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

benchmark_buttons_frame = tk.Frame(content2, bg="#9300FF")
benchmark_buttons_frame.pack()

compute_performance_label = tk.Label(benchmark_buttons_frame, text="Individual Benchmarks", font=text_font, bg="#9300FF",
                                        bd=15, relief="groove")
compute_performance_label.pack(side=tk.TOP)

# Matrix Multiplication section
compute_matrix_multip_button = tk.Button(benchmark_buttons_frame, text="Compute Matrix Multiplication", command=compute_matrix_multip, bg="#d0d0d0", font=button_font,bd=5)
compute_matrix_multip_button.pack(pady=5)

def matLabel():
    resultMat_label.config(text="", bg="#9300FF", font=text_font)

resultMat_label = tk.Label(content2, text="", bg="#9300FF", font=text_font)
resultMat_label.pack(pady=5)

# Button to display Pi section
display_pi_button = tk.Button(benchmark_buttons_frame, text="Pi", command=show_pi_section, bg="#d0d0d0", font=button_font,bd=5)
display_pi_button.pack(pady=5)

# Pi section
pi_section = tk.Frame(content2, borderwidth=2, bg="#ffffff", bd=20, relief="groove")

digits_label = tk.Label(pi_section, text="Enter the number of digits of Pi to calculate:", font=text_font, bg="#ffffff")
digits_label.pack()

digits_entry = tk.Entry(pi_section, font=("Arial", 12))
digits_entry.pack()

compute_pi_button = tk.Button(pi_section, text="Compute Pi", command=compute_pi, bg="#d0d0d0", font=button_font)
compute_pi_button.pack(pady=5)

compute_pi_button2 = tk.Button(pi_section, text="Plot Powers of Pi", command=compute_pi_powers, bg="#d0d0d0", font=button_font)
compute_pi_button2.pack(pady=5)

resultPI_label = tk.Label(pi_section, text="", font=text_font, bg="#ffffff")
resultPI_label.pack(pady=5)

cancel_pi_button = tk.Button(pi_section, text="Cancel", command=hide_pi_section, bg="#d0d0d0", font=button_font)
cancel_pi_button.pack(pady=5)

# Button to display Read/Write Speed section
display_rw_button = tk.Button(benchmark_buttons_frame, text="Read/Write Speed", command=show_rw_section, bg="#d0d0d0", font=button_font, bd=5)
display_rw_button.pack(pady=5)

# Read/Write Speed section
rw_section = tk.Frame(content2, borderwidth=2, bg="#ffffff", bd=20, relief="groove")

mb_label = tk.Label(rw_section, text="Enter the number of MB to benchmark:", font=text_font, bg="#ffffff")
mb_label.pack()

mb_entry = tk.Entry(rw_section, font=text_font)
mb_entry.pack()

compute_speed_button = tk.Button(rw_section, text="Compute Read/Write Speed", command=compute_rw, bg="#d0d0d0", font=button_font)
compute_speed_button.pack(pady=5)

resultRW_label = tk.Label(rw_section, text="", font=text_font, bg="#ffffff")
resultRW_label.pack(pady=5)

cancel_rw_button = tk.Button(rw_section, text="Cancel", command=hide_rw_section, bg="#d0d0d0", font=button_font)
cancel_rw_button.pack(pady=5)

# Content 3 - Computer Specs
content3 = tk.Frame(root, bg="#9300FF", bd=150, relief="groove")
label3 = tk.Label(content3, text='Current Specs: \n' + str(specsString), font=("Lucida Console",12), bg="#ffffff")
label3.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Content 4 - History

def updateHistory():

    for item in tree.get_children():
        tree.delete(item)

    history_entries = hs.read_history_csv()
    if history_entries:
        for entry in history_entries:
            tree.insert("", "end", values=entry)

content4 = tk.Frame(root, bg="#9300FF", bd=2, relief="groove")
label4 = tk.Label(content4, text='History', font=text_font, bg="#9300FF",bd=10, relief="groove")
label4.pack(fill=tk.BOTH, expand=False)

style = ttk.Style()
style.configure("Treeview", background="#d0d0d0", font=text_font, borderwidth=2, relief="groove")
tree = ttk.Treeview(content4, columns=("OS", "RAM", "CPU", "GPU", "SCORE"), show="headings",style="Treeview")

tree.heading("OS", text="OS")
tree.heading("CPU", text="RAM")
tree.heading("RAM", text="CPU")
tree.heading("GPU", text="GPU")
tree.heading("SCORE", text="SCORE")

tree.column("OS", anchor=tk.CENTER, width=5)
tree.column("CPU", anchor=tk.CENTER, width=5)
tree.column("RAM", anchor=tk.CENTER, width=150)
tree.column("GPU", anchor=tk.CENTER, width=150)
tree.column("SCORE", anchor=tk.CENTER, width=5)

# Pack the Treeview
tree.pack(expand=True, fill="both")

# Function to exit the application
def exit_app():
    print("Exit button clicked")
    root.quit()

# Pack default content initially
default_content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
current_content = default_content

# Create a frame for button list
button_frame = tk.Frame(root, bg="#B6B2B9")
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Buttons for navigation
button1 = tk.Button(button_frame, text='About the app', command=lambda: switch_content(content1), bg="#d0d0d0", font=button_font)
button2 = tk.Button(button_frame, text='Benchmarking', command=lambda: switch_content(content2), bg="#d0d0d0", font=button_font)
button3 = tk.Button(button_frame, text='Computer Information', command=lambda: switch_content(content3), bg="#d0d0d0", font=button_font)
button4 = tk.Button(button_frame, text='History', command=lambda: switch_content(content4), bg="#d0d0d0", font=button_font)
exit_button = tk.Button(button_frame, text='Exit', command=exit_app, bg="#d0d0d0", font=button_font)

# Pack buttons
button1.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button2.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button3.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
button4.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
exit_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Bind hover effects to buttons
buttons = [button1, button2, button3, button4, exit_button, compute_matrix_multip_button, display_pi_button, compute_pi_button, compute_pi_button2, cancel_pi_button, display_rw_button, compute_speed_button, cancel_rw_button,run_benchmark_button]
for btn in buttons:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

if __name__ == '__main__':
    root.mainloop()
