import pandas as pd
from tkinter.filedialog import askopenfilename

def get_file_path():
    return askopenfilename(title="Select Fulfillment - Loans Returns and Overdue Dashboard", filetypes=[("Fulfillment Report", "*.xlsx")])

file_path = get_file_path()

df = pd.read_excel(file_path, header=None)
df_data = df.iloc[13:]

for index, row in df_data.iterrows():
    print(f"Row {index}: {row.tolist()}")