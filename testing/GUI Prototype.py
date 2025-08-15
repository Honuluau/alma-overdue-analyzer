from tkinter import *
from tkinter.filedialog import askopenfilename
import datetime
import os
import webview

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

class API:
    def __init__(self):
        self.window = None

        def change_text(self):
            self.window.evaluate_js("document.getElementById('last_update').innerText = 'Last Update: Test'")


api = API()
file_path = os.path.abspath("web/index.html")
api.window = webview.create_window("Alma Overdue Analyzer", file_path, width=700, height=400)
webview.start()