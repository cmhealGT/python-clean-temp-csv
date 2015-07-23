import pandas
import time

def convert_to_center(full_text):
    text_as_string = str(full_text)
    last_six = text_as_string[-6:]
    if(last_six == "Center"):
        text_as_string = last_six
    return text_as_string

def convert_to_top(full_text):
    text_as_string = str(full_text)
    last_three = text_as_string[-3:]
    if(last_three == "Top"):
        text_as_string = last_three
    return text_as_string

def convert_to_rack(full_text):
    text_as_string = str(full_text)
    last_seven= text_as_string[-7:]
    return last_seven

filename="Raw"    
df=pandas.read_csv(filename+".csv")
#print
df = df.rename(columns={'Sensor': 'Sensor Position', 'Location': 'Rack Number', 'Value':'Value (degF)'})

df['Sensor Position']=df['Sensor Position'].apply(convert_to_center)
df['Sensor Position']=df['Sensor Position'].apply(convert_to_top)
df['Rack Number']=df['Rack Number'].apply(convert_to_rack)
del df['Units']
del df['Status']
del df['Device']
del df['Parent Device']

df.to_csv("Clean.csv", index=False)