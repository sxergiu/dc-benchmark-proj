def compute_matrix_multip():
    resultMat_label.config(text="Computing matrix operations...")
    display_pi_button.config(state=tk.DISABLED)
    display_rw_button.config(state=tk.DISABLED)
    thread = threading.Thread(target=mat_wrapper)  # Use a thread to run mat() function
    thread.start()