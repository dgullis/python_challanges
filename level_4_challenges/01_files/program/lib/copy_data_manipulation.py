import os


# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    return os.path.exists(filename)
    

# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
import pandas as pd

def get_file_contents(filename):
    contents = pd.read_csv(filename, index_col=0)
    print(contents)

# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    with open(filename, 'r') as file:
        contents = file.readlines()
        christmas_day_contents = [item for item in contents if item[0:5] == '25/12']

        if include_header_row:
            return [contents[0]] + christmas_day_contents
        else:
            return christmas_day_contents
        
# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    with open(filename, 'r') as file:
        contents = file.readlines()
        christmas_day_contents = [item for item in contents if item[0:5] == '25/12']

        christmas_day_contents_split = [item.split(';') for item in christmas_day_contents]
    
        christmas_day_air_quality_values = [int(item[3]) for item in christmas_day_contents_split]

        average_christmas_day_air_quality_values = sum(christmas_day_air_quality_values) / len(christmas_day_air_quality_values)
        return round(average_christmas_day_air_quality_values, 2)

# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    
    with open(filename, 'r') as file:
        contents = file.readlines()
        months = ['01', '02', '03', '04', '05', '06', '05', '08', '09', '10', '11', '12']
        month_data_raw = {month: [] for month in months}
        
        for item in contents:
            month = item[3:5]
            if month in months:
                month_data_raw[month].append(list(map(int, item.split(';')[3].split(', '))))
        
        averages = {int(month): round(sum(sum(data) for data in month_data_raw[month]) / len(month_data_raw[month]), 2) for month in months}
        
        return averages
        

# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    with open(filename, 'r') as file:
        contents = file.readlines()
    
    march_data = [item for item in contents if item[3:5] == '03']
    
    new_file = open('AirQualityMarch.csv', 'w')
    new_file.write(contents[0])
    
    for line in march_data:
        new_file.write(line)



# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    
    os.mkdir("/Users/dangullis/python_foundations/extension_challenges/01_files/program/monthly_responses")
    
    with open(filename, 'r') as file:
        contents = file.readlines()
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        raw_data = {
            '2004': {month: [] for month in months},
            '2005': {month: [] for month in months}
        }
    
    path = "/Users/dangullis/python_foundations/extension_challenges/01_files/program/monthly_responses/"

    for item in contents:
        year = item[6:10]
        month = item[3:5]
        if month in months:
            raw_data[year][month].append(item)
    
    new_dict = {key: {key1: value1 for key1, value1 in value.items() if value1} for key, value in raw_data.items()}
    
    for year, year_data in new_dict.items():
        for month, month_data in year_data.items():
            if month_data:
                file_path = os.path.join(path, f"{month}-{year}.csv")
                with open(file_path, 'w') as file:
                    file.write(contents[0])
                    file.writelines(month_data)