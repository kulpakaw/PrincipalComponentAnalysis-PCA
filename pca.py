import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def csv_to_dataframe(file_path):
    """
    Reads a CSV file and returns its contents as a pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path, sep=";")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return pd.DataFrame()

file_path = "Dane/student_mat.csv"
data = csv_to_dataframe(file_path)
print(data.head())

