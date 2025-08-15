from tkinter import *
from tkinter.filedialog import askopenfilename

window = Tk()

filename = askopenfilename(title="Select Fulfillment - Loans Returns and Overdue Dashboard", filetypes=[("Fulfillment Report", "*.xlsx")])
print(filename)

window.mainloop()