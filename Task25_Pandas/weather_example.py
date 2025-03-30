import csv
import pandas

# Writing csv files
with open("weather.csv") as data_file:
    data = csv.reader(data_file)
    all_temperatures = []
    for row in data:
        print(row)

# Using pandas is much simpler
print(data["temp"])
# Check the type of data, series is a column - like a list
type(data["temp"])
# Use data as a dictionary
data_dict = data.to_dict()
print(data_dict)

# Change data to a list
temp_list = data["temp"].to_list()
# It can be used the first line as name for the list without declaring it
temp_list2 = data.temp

# Save day of higher temp
for weather in data:
    if weather.temp == weather.temp.max:
        day_temp_high = weather.temp


# Save data in a csv file
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [115, 32, 22]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")