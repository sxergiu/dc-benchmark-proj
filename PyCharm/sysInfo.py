import platform
import subprocess

def get_processor():
    system = platform.system()
    if system == "Windows":
        try:
            output = subprocess.check_output(["wmic", "cpu", "get", "name"]).decode().strip().split("\n")[1]
            return output
        except Exception as e:
            return str(e)
    else:
        processor_info = platform.processor()
        if "Intel" in processor_info:
            model = processor_info.split(" ")[3:]
            return " ".join(model)
        elif "AMD" in processor_info:
            model = processor_info.split(" ")[2:]
            return " ".join(model)
        else:
            return processor_info

def get_operating_system():
    system = platform.system()
    if system == "Windows":
        try:
            release = platform.release()
            if release == "11":
                return "Windows 11"
            else:
                return f"Windows {release}"
        except Exception as e:
            return "Unknown Windows Version"
    else:
        return system

def get_total_ram():
    import psutil
    return f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"

def get_gpu():
    try:
        import pycuda.driver as cuda
        cuda.init()
        device = cuda.Device(0)
        return device.name().strip()
    except ImportError:
        print("pycuda is not installed.")
    except Exception as e:
        print(f"Error with pycuda: {e}")

    # Try to detect Intel GPU using platform module on Windows
    if platform.system() == "Windows":
        try:
            output = subprocess.check_output(["wmic", "path", "win32_videocontroller", "get", "name"]).decode().strip().split("\n")[1]
            return output
        except Exception as e:
            print(f"Error with platform module: {e}")

    return "No GPU detected"

if __name__ == "__main__":
    print("Processor Model:", get_processor())
    print("Operating System:", get_operating_system())
    print("Total RAM:", get_total_ram())
    print("GPU:", get_gpu())
