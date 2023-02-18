import tkinter
from tkinter import *
from PIL import Image,ImageTk
import requests
import json

root = Tk()
root.title('Air Quality Monitor')
root.iconbitmap('')

api_requests = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89120&distance=5&API_KEY=4D852C1B-5881-467D-B9F3-24FF8CAE46BA')
api = json.loads(api_requests.content)

try :
    api_requests = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89120&distance=5&API_KEY=4D852C1B-5881-467D-B9F3-24FF8CAE46BA')
    api = json.loads(api_requests.content)
    report_area = api[0]['ReportingArea']
    State_Code = api[0]['StateCode']
    Latitude = api[0]['Latitude']
    Quality = api[0]['Category']['Name']

    if Quality == 'Good':
        wheather_colour1 = '#00FF00'
    elif Quality == 'Moderate':
        wheather_colour1 == '#FCFF00'
    elif Quality == 'Unhealthy for Sensitive Groups':
        wheather_colour1 == '#FF7F00'
    elif Quality == 'Unhealthy':
        wheather_colour1 == '#FF001E'
    elif Quality == 'Very Unhealthy':
        wheather_colour1== '#C400FF'
    elif Quality == 'Hazardous':
        wheather_colour1== '#701111'
    else :
        wheather_colour1 == 'white'
    reportarea = tkinter.Label(root, text=report_area)
    reportarea.grid(row=0, column=0)

    StateCode = tkinter.Label(root, text=State_Code)
    StateCode.grid(row=0, column=1)

    Latitude1 = tkinter.Label(root, text=Latitude)
    Latitude1.grid(row=0, column=2)

    Quality1 = tkinter.Label(root, text=Quality,bg=wheather_colour1)
    Quality1.grid(row=0, column=3)

except Exception as e :
    api = "Error .."
    print(api)

root.mainloop()
