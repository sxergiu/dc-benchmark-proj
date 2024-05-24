import tkinter as tk
from tkinter import ttk
import csv
import os

def read_history_csv():
    # Check if "History.csv" exists in the current directory
    if not os.path.exists("PyCharm/Benchmarks/History.csv"):
        print("History.csv not found in the project directory.")
        return None

    # Array to store entries
    entries = []

    # Open the CSV file for reading
    with open("PyCharm/Benchmarks/History.csv", "r") as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Extract information from the row
            os_info = row["Operating system"]
            cpu_info = row["CPU"]
            ram_info = row["Total RAM"]
            gpu_info = row["GPU"]
            score_info = row["SCORE"]

            # Store the information as a tuple
            entry = (os_info,cpu_info, ram_info, gpu_info, score_info)

            # Append the entry to the array
            entries.append(entry)

    return entries

