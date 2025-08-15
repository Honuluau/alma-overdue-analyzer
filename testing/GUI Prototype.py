from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime

def get_file_path():
    return askopenfilename(title="Select Fulfillment - Loans Returns and Overdue Dashboard", filetypes=[("Fulfillment Report", "*.xlsx")])

def log(log_type, message):
    try:
        with open("log/log.txt", 'a+') as f:
            current_datetime = datetime.datetime.now()
            f.writelines(f"\n[{current_datetime.strftime("%Y-%m-%d %H:%M:%S")}][{log_type}] {message}")
    except Exception as e:
        print(f"An error has occurred: {e}")

def get_last_run_time():
    try:
        with open("log/log.txt") as f:
            lines = f.readlines()
            last_run_time = None
            for line in lines[::-1]:
                if "RAN" in line:
                    last_run_time = line.split("]")[0].strip("[]")
                    break

            f.close()

            if last_run_time is None:
                log("ERROR", "Error code 2. None returned.")

            return last_run_time

    except Exception as e:
        log("ERROR", f"Error code 1. {e}")

def main():
    last_run_time = get_last_run_time()
    print(last_run_time)

main()

window = Tk()

window.mainloop()