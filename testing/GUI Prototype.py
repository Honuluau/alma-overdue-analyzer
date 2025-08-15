from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime

def get_file_path():
    return askopenfilename(title="Select Fulfillment - Loans Returns and Overdue Dashboard", filetypes=[("Fulfillment Report", "*.xlsx")])

def open_fulfillment():
    file_path = get_file_path()

def log(log_type, message):
    try:
        with open("log/log.txt", 'a+') as f:
            current_datetime = datetime.datetime.now()
            f.writelines(f"\n[{current_datetime.strftime("%Y-%m-%d %H:%M:%S")}][{log_type}] {message}")
    except Exception as e:
        print(f"An error has occurred: {e}")

def fake_update_for_test():
    log("UPDATE", "This is fake for a test.")
    update_time_label.config(text=f"Last updated: {get_last_update_time()}")

def get_last_update_time():
    try:
        with open("log/log.txt") as f:
            lines = f.readlines()
            last_run_time = None
            for line in lines[::-1]:
                if "UPDATE" in line:
                    last_run_time = line.split("]")[0].strip("[]")
                    break

            f.close()

            if last_run_time is None:
                log("ERROR", "Error code 2. None returned, using arbitrary date.")
                return "2007-08-31 01:00:39"

            return last_run_time

    except Exception as e:
        log("ERROR", f"Error code 1. {e}")

def main():
    print("main lol")

window = Tk()
window.title("Alma Overdue Analyzer")

menubar = Menu(window)
window.config(menu=menubar)
window.geometry("700x400")

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_fulfillment)
file_menu.add_command(label="FAKE UPDATE", command=fake_update_for_test)

update_frame = Frame(window)
update_frame.pack()

update_time_label = Label(update_frame, justify=CENTER,text=f"Last updated: {get_last_update_time()}")
update_time_label.pack()

main()
window.mainloop()