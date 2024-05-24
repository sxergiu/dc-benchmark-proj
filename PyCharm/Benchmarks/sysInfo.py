import platform
import subprocess
import psutil
import os
import pandas as pd


def get_os_info():
    """Get the operating system information."""
    os_info = platform.system()
    if os_info == "Windows":
        try:
            release = platform.release()
            version = platform.version()
            return f"Windows {release} (Version {version})"
        except Exception as e:
            return f"Error getting Windows version: {e}"
    elif os_info == "Linux":
        try:
            distro = platform.linux_distribution()
            return f"{distro[0]} {distro[1]} {distro[2]}"
        except AttributeError:
            return "Linux (specific distribution detection not supported)"
        except Exception as e:
            return f"Error getting Linux distribution: {e}"
    elif os_info == "Darwin":
        try:
            mac_ver = platform.mac_ver()
            return f"macOS {mac_ver[0]}"
        except Exception as e:
            return f"Error getting macOS version: {e}"
    else:
        return f"Unsupported OS: {os_info}"

def get_ram_info():
    """Get the total RAM information."""
    try:
        total_ram = psutil.virtual_memory().total
        return f"{total_ram / (1024 ** 3):.2f} GB"
    except Exception as e:
        return f"Error getting RAM information: {e}"

def get_cpu_info():
    """Get the CPU information."""
    try:
        cpu_info = platform.processor()
        if not cpu_info:  # If platform.processor() returns an empty string
            cpu_info = subprocess.check_output(["lscpu"]).decode().strip().split("\n")
            cpu_info = [line for line in cpu_info if "Model name:" in line][0].split(":")[1].strip()
        return cpu_info
    except Exception as e:
        return f"Error getting CPU information: {e}"

def get_gpu_info():
    """Get the GPU information."""
    os_info = platform.system()
    if os_info == "Windows":
        try:
            output = subprocess.check_output(["wmic", "path", "win32_videocontroller", "get", "name"]).decode().strip().split("\n")
            return ", ".join([line.strip() for line in output if line.strip()][1:])
        except Exception as e:
            return f"Error getting GPU information on Windows: {e}"
    elif os_info == "Linux":
        try:
            output = subprocess.check_output(["lspci", "-nnk"]).decode().strip().split("\n")
            gpu_lines = [line for line in output if "VGA compatible controller" in line]
            return ", ".join(gpu_lines)
        except Exception as e:
            return f"Error getting GPU information on Linux: {e}"
    elif os_info == "Darwin":  # macOS
        try:
            output = subprocess.check_output(["system_profiler", "SPDisplaysDataType"]).decode().strip().split("\n")
            gpu_lines = [line.strip() for line in output if "Chipset Model" in line]
            return ", ".join(gpu_lines)
        except Exception as e:
            return f"Error getting GPU information on macOS: {e}"
    else:
        return "No GPU detected or unsupported operating system"

def get_system_info():
    """Get all system information."""
    os_info = get_os_info()
    ram_info = get_ram_info()
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()

    info = [ os_info, cpu_info, ram_info, gpu_info ]

    return f"Operating System: {os_info}\nCPU: {cpu_info}\nTotal RAM: {ram_info}\nGPU: {gpu_info}\n",info


def write_in_file(info):
    header = ['Operating system', 'CPU', 'Total RAM', 'GPU', 'SCORE']
    file_path = "PyCharm/Benchmarks/History.csv"

    # Check if the file exists
    file_exists = os.path.exists(file_path)

    # Check if the file is empty
    if file_exists:
        is_empty = os.path.getsize(file_path) == 0
    else:
        is_empty = True

    # If the file doesn't exist or is empty, write the headers
    if is_empty:
        with open(file_path, mode='w', newline='') as file:
            df = pd.DataFrame(columns=header)
            df.to_csv(file, header=True, index=False)

    # Append the new data to the file
    new_data = pd.DataFrame([info], columns=header)
    new_data.to_csv(file_path, mode='a', header=False, index=False)

if __name__ == "__main__":
    print(get_system_info())