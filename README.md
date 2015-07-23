# python-clean-temp-csv
This is a script to clean the temperature sensor data.

## Primary Tasks
- Create a 'cleaned' file
- Remove uninformative columns
- Short descriptions of racks
- Convert timestamp text to some numeric standard (perhaps unnecessary)

## Inputs from file
- Device (usually a combination of room, rack, device, and IP address)
  -   ex. Data Center Rack 18 Feed B (Utility) rPDU(10.169.3.131)
- Parent Device (I believe a collection)
  -   ex. BOCDCE (StruxureWare Data Center Expert)
- Sensor (type of sensor - in this example always temperature, but I'm sure other types could be encountered)
  -   ex. Temperature - Rack Inlet - Center
- Location (usually a rack number - somewhat redundant with Device)
  -   ex. BOC Data Center Rack 18
- Time
  -   ex. Jun 22, 2015 3:15:37 PM
- Value
  -   ex. 78.4
- Units
  -   ex. deg F
- Status
  -   (in this case blank)

## Outputs
The idea is to simplify the output, remove redundancies, and manipulate the timestamps to a reasonable level.
- Sensor Position
  -   ex. Center or Top
- Rack Number
  -   ex. Rack 18
- Time (number of seconds from January 1, 1970 -- a relatively standard format that can be transformed into date, time, day of the week, weekday/weekend, AM/PM, etc.)
  -   ex. 1137056501
- Value
  -   ex. 78.4
