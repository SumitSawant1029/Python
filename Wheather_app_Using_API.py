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
