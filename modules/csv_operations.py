import pandas as pd

def calculate_csv_data(csv_file_path, name_column, hours_column):
    """ Take CSV File, Staff Columnm and Hours Column, returns each staff member with their total hours. """
    dataFrame = pd.read_csv(csv_file_path)
    finalData = dataFrame.groupby(['staff'], sort = True)['shift time ex. break (hr)'].sum()

    return finalData
