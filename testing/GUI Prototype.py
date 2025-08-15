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
    except FileExistsError:
        print(f"File already exists.")
    except Exception as e:
        print(f"An error has occurred: {e}")

def main():
    log("TEST", "This is a test")

main()

window = Tk()

window.mainloop()