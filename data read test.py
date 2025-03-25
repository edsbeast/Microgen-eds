import os
import pandas as pd
import matplotlib.pyplot as plt


folder_path = 'C:/Users/eds5328/Downloads/TL_LEDO6060_2xSand15mm.zip/TL_LEDO6060_2xSand15mm'
x_label = "Frequency"
y_label = "20*log10(u_out_center/u_in)"


def read_txt(folder_path, skip_rows, columns, nrows, name, iso):
    txt_data = {"Frequency": [], "20*log10(u_out_center/u_in)": []}
    avg_data = {"Frequency": [], "20*log10(u_out_center/u_in)": []}
    for filename in os.listdr(folder_path):
        seg_name_1 = filename.split('.txt')
        seg_name = seg_name_1[0].split('_')
        if seg_name[0] == name and seg_name[2] == iso:
            file_path = os.path.join(folder_path, filename)
            txt_append = pd.read_csv(file_path, delimiter='\t', skiprows=skip_rows, usecols=columns, nrows=nrows)
            txt_data = txt_data.append(txt_append)
    return txt_data

def read_csv(folder_path, title):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            seg_name = filename.split('_')
            csv_data = pd.read_csv(file_path, skiprows = 5)
    return [csv_data, seg_name]
            
