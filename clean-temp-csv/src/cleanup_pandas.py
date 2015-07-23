import pandas
from datetime import datetime

# all center locations are labeled ending in "Center", so I retain only the last 6 characters in the string
def convert_to_center(full_text):
    text_as_string = str(full_text)
    last_six = text_as_string[-6:]
    if(last_six == "Center"):
        text_as_string = last_six
    return text_as_string

# all top locations are labeled ending in "Top", so I retain only the last 3 characters in the string
def convert_to_top(full_text):
    text_as_string = str(full_text)
    last_three = text_as_string[-3:]
    if(last_three == "Top"):
        text_as_string = last_three
    return text_as_string

# all racks are labeled ending in "Rack XX", so I retain only the last 7 characters in the string 
def convert_to_rack(full_text):
    text_as_string = str(full_text)
    last_seven = text_as_string[-7:]
    return last_seven

# time format example: Jun 22, 2015 3:15:37 PM
def convert_to_seconds_time(full_text):
    time_value = str(full_text)
    value = datetime.strptime(time_value, "%b %d, %Y %I:%M:%S %p");
    return (value - datetime(1970, 1, 1)).total_seconds();

filename = "Raw"    
df = pandas.read_csv("Raw.csv")

# rename columns
df = df.rename(columns={'Sensor': 'Sensor Position', 'Location': 'Rack Number', 'Value':'Value (degF)'})

# remove unneeded text
df['Sensor Position'] = df['Sensor Position'].apply(convert_to_center)
df['Sensor Position'] = df['Sensor Position'].apply(convert_to_top)
df['Rack Number'] = df['Rack Number'].apply(convert_to_rack)

# delete unneeded columns (inspected visually, not checked in the code)
# there should be a nice way to do this automatically, but I'm not going to do this now
del df['Units']
del df['Status']
del df['Device']
del df['Parent Device']

# convert time stamps to columns for year, month, day, hour, minute, second, day of week
# old format (Jun 22, 2015 3:15:37 PM)
# I think all data processing environments can process time, so I'm probably going to leave this like the old version.
df['Time'] = df['Time'].apply(convert_to_seconds_time)

df.to_csv("Clean.csv", index=False)
