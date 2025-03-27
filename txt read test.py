import os
import pandas as pd
import matplotlib.pyplot as plt

names_lst = ['Diamond', 'FRD', 'Gyroid', 'IWP', 'Lidinoid', 'Neovius', 'PDFRD', 'PSPIWP', 'SchwarzP', 'SplitP']

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

def read_txt(folder_path, skip_rows, columns, nrows, name, iso, name_data):
    txt_data = pd.DataFrame({})
    for filename in os.listdir(folder_path):
        seg_name_1 = filename.split('.txt')
        seg_name = seg_name_1[0].split('_')
        if seg_name[0] == name and seg_name[2] == iso:
            print(filename)
            file_path = os.path.join(folder_path, filename)
            txt_append = pd.read_csv(file_path, delimiter='\t', skiprows=skip_rows, usecols=columns, nrows=nrows)
            txt_data = txt_data._append(txt_append, ignore_index = True)
    txt_data.columns = ['Frequency', 'Data']
    return txt_data

#use_cols = [1,2]
#skip_rows = 83
#name = 'C:/Users/eds5328/Downloads/Diamond/Diamond'
#name_data = names_get(names_lst)
#df = read_txt(name,skip_rows,use_cols,6401,'Diamond','0.1875ISO', name_data)
#print(df)

st = '0.1233ISO'
st = st +'0'
print(st)
'''
plt.figure(figsize=(10, 6))

# Plot the first 6400 entries from column 'Y1'
plt.plot(df['X'][:6400], df['File 1 Data'], label='First 6400 entries')

# Plot the next 6400 entries from column 'Y2'
plt.plot(df['X'][6400:12800], df['File 2 Data'], label='Next 6400 entries')

# Plot the final 6400 entries from column 'Y3'
plt.plot(df['X'][12800:], df['File 3 Data'], label='Final 6400 entries')

# Adding labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Plot of DataFrame Columns')
plt.legend()

# Show the plot
plt.show()
'''
