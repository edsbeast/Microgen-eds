import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder_path = 'C:/Users/eds5328/Downloads/Diamond/Diamond'
names_lst = ['Diamond', 'FRD', 'Gyroid', 'IWP', 'Lidinoid', 'Neovius', 'PDFRD', 'PSPIWP', 'SchwarzP', 'SplitP']
names_test = ['FRD']
def names_get(names_lst):
    names = pd.DataFrame({'Diamond': [], 'FRD': [], 'Gyroid': [], 'IWP': [], 'Lidinoid': [], 'Neovius': [], 'PDFRD': [], 'PSPIWP': [], 'SchwarzP': [], 'SplitP': []})
    for name in names_lst:
        folder_path = f'C:/Users/eds5328/Downloads/{name}/{name}'
        for filename in os.listdir(folder_path):
            seg_name_1 = filename.split('.txt')
            seg_name = seg_name_1[0].split('_')
            model_type = seg_name[0]
            iso_value = seg_name[2]
            new_data = {f'{model_type}': f'{iso_value}'}
            names = names._append(new_data, ignore_index =True)
    return names

def read_csv(folder_path, name, iso):
    csv_data = False
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            seg_name = filename.split('_')
            csv_name = seg_name[0]
            if csv_name == 'PDFRD' or 'PSPIWP':
                csv_iso = seg_name[1]
            else:
                csv_iso = seg_name[1]
            if len(csv_iso) == 8:
                splt_iso = csv_iso.split('ISO')
                splt_iso[0] = splt_iso[0] + '0'
                csv_iso = splt_iso[0] + splt_iso[1]
            if csv_iso == iso and csv_name == name:
                file_path = os.path.join(folder_path, filename)
                csv_data = pd.read_csv(file_path, skiprows = 5)
    return csv_data

def read_txt(names_lst, skip_rows, columns, nrows, name_data):
    txt_data = pd.DataFrame({})
    for name in names_lst:
        folder_path = f'C:/Users/eds5328/Downloads/{name}/{name}'
        for filename in os.listdir(folder_path):
            seg_name_1 = filename.split('.txt')
            seg_name = seg_name_1[0].split('_')
            name = seg_name[0]
            iso = seg_name[len(seg_name)-2]
            if name_data[name].isin([iso]).any():
                file_path = os.path.join(folder_path, filename)
                txt_append = pd.read_csv(file_path, delimiter='\t', skiprows=skip_rows, usecols=columns, nrows=nrows)
                txt_data = txt_data._append(txt_append, ignore_index = True)
                if seg_name[len(seg_name)-1] == '3':
                    txt_data.columns = ['Frequency', 'Data']
                    csv_data = read_csv('C:/Users/eds5328/Downloads/Simulation/TL_LEDO6060_2xSand15mm',name,iso)
                    if csv_data is not False:
                        plt.plot(csv_data.iloc[:,0], csv_data.iloc[:,1], label = 'Simulation Data', color = 'orange')
                        x = txt_data.iloc[:3001, 0]
                        y1 = txt_data.iloc[:3001, 1]
                        y2 = txt_data.iloc[3001:6002, 1]
                        y3 = txt_data.iloc[6002:, 1]
                        input_df = pd.read_csv("C:/Users/eds5328/Downloads/reference_shaker.txt", delimiter='\t', skiprows=skip_rows, usecols=columns, nrows=nrows)
                        input_df = input_df.iloc[:3001, 1]
                        y1 = y1 / input_df
                        y1 = abs(y1)
                        y1 = 20 * np.log(y1)
                        y2=y2.reset_index(drop=True)
                        y3=y3.reset_index(drop=True)
                        y2 = y2 / input_df
                        y2 = abs(y2)
                        y2 = 20 * np.log(y2)
                        y3 = y3 / input_df
                        y3 = abs(y3)
                        y3 = 20 * np.log(y3)
                        concatenated_df = pd.concat([y1.reset_index(drop=True), y2.reset_index(drop=True), y3.reset_index(drop=True)], axis=1)
                        plt.plot(x, concatenated_df.iloc[:3001, 0], label='Exp Data 1', color='blue')
                        plt.plot(x, concatenated_df.iloc[:3001, 1], label='Exp Data 2', color='green')
                        plt.plot(x, concatenated_df.iloc[:3001, 2], label='Exp Data 3', color='red')
                        std_dev_df = concatenated_df.std(axis=1)
                        y_avg = concatenated_df.mean(axis=1)
                        plt.fill_between(x, y_avg - std_dev_df, y_avg + std_dev_df, color='cyan', alpha=0.3, label='Standard Deviation')
                        plt.plot(x, y_avg, label='Average', color='black', linestyle='--')
                        plt.xlabel('Frequency')
                        plt.ylabel('')
                        plt.title(f'{name} at {iso}')
                        plt.legend()
                        plt.show()
                    txt_data = pd.DataFrame({})
    return txt_data
#"C:\Users\eds5328\Downloads\reference_shaker.txt"
#20*log10(u_out_center/u_in)
use_cols = [1,2]
skip_rows = 83
name_data = names_get(names_lst)
df = read_txt(names_lst,skip_rows,use_cols,3001, name_data)
