#!/usr/bin/env python
# coding: utf-8

#               Development of Weather App with Python

# Importing all necessary modules for the development of the App

# In[1934]:


from tkinter import *


# In[1935]:


import tkinter as tk


# The above line of code imports all classes, functions, and variables from the tkinter module, allowing for easy access to its entire library of graphical user interface tools.

# In[1936]:


from geopy.geocoders import Nominatim


# This above code imports the Nominatim class from the geocoders module in the Geopy library, which provides tools for geocoding and reverse geocoding, i.e., converting addresses to geographic coordinates and vice versa.

# In[1937]:


from tkinter import ttk, messagebox


# The above code imports both the ttk module and the messagebox module from the tkinter library, which allows for creating themed widgets and displaying pop-up message boxes in GUI applications.

# In[1938]:


from timezonefinder import TimezoneFinder


# The above code imports the TimezoneFinder class from the timezonefinder module, which provides a simple way of determining the time zone for a given latitude and longitude using OpenStreetMap data.

# In[1939]:


from datetime import datetime


# The above code imports the datetime class from the datetime module, which provides functionality for working with dates and times in Python.

# In[1940]:


import requests


# This imports the requests library, which allows for making HTTP requests in Python, including sending and receiving data from web servers.

# In[1941]:


import pytz


# This imports the pytz module, which is a third-party Python library used for working with time zones. It provides timezone definitions, datetime manipulation, and localization capabilities.

# In[1942]:


root = Tk()


# In[1943]:


root.title("Weather App")


# In[1944]:


root.geometry("900x500+300+200")


# In[1945]:


root.resizable(False,False)


# The above codes creates a new main window for a GUI application, setting the window title to "Weather App", specifying the window's dimensions and position on the screen, and disabl resizing of the window in both dimensions using the resizable() method.

# In[1946]:


def getWeather():
    city=textfield.get()
    try:
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat = location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRRENT WEATHER")
    
        #Weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=76bd0826d73c858f9a56f1bfd778736f"
    
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]["description"]
        temp = int(json_data["main"]["temp"]-273.15)
        pressure = json_data["main"]['pressure']
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
    
        t.config(text = (temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror('Weather App',"Invalid Entry!!")
    


# The above codes defines a function called getWeather() that retrieves the current weather and time information for a given city. It first gets the city name entered from the textfield. Then, it uses the geopy library to get the latitude and longitude of the city, which is used to get the timezone of the city using the TimezoneFinder module from pytz.
# 
# After getting the timezone, it uses the datetime module from pytz to get the current time in that timezone, which is displayed on a clock widget in the GUI. The api variable contains the OpenWeatherMap API URL with the city name entered by the user as a parameter, which is used to get the current weather data for that city.
# 
# The weather data is then parsed from the JSON response using the json module from the requests library. Finally, the temperature, condition, wind speed, humidity, pressure, and description are displayed on their respective widgets in the GUI.
# 
# If there is any exception encountered while running the code, such as invalid user input, a messagebox is displayed with an error message indicating "Invalid Entry!!". This function is designed to be used as a part of my weather app project.

# Search Box

# In[1947]:


Search_image = PhotoImage(file = "search.png")


# In[1948]:


image = Label(image = Search_image)


# In[1949]:


image.place(x = 20, y = 20)


# The abbove codes load an image file and use it to create a Tkinter Label widget. The widget is positioned on the window at coordinates (20, 20) using the place geometry manager.

# In[1950]:


textfield = tk.Entry(root,justify ='center',width=17,font=("Verdana",25,"bold"),bg= "#444444", border=0, fg = "#D3D3D3")


# In[1951]:


textfield.place(x=45, y=40)


# In[1952]:


textfield.focus()


# The above code creates an entry widget with a dark grey background, places it on a tkinter window or frame at position (45, 40), and sets the focus on the widget.

# In[1953]:


Search_icon = PhotoImage(file = "search_icon.png")


# In[1954]:


myimage_icon = Button(image= Search_icon, borderwidth=0, cursor="hand2",bg="#404040",command=getWeather)


# In[1955]:


myimage_icon.place(x=400,y=34)


# This code creates a button with an image of a search icon, places it on a tkinter window or frame at position (400, 34), and sets the background color of the button to dark grey.

# Logo

# In[1956]:


Logo_image=PhotoImage(file="logo.png")


# In[1957]:


logo=Label(image=Logo_image)


# In[1958]:


logo.place(x=150,y=100)


# The above code loads an image file of a logo, creates a label with the logo image, and places the label on a tkinter window or frame at position (150, 100).

# Bottom Box

# In[1959]:


Frame_image=PhotoImage(file="box.png")


# In[1960]:


frame_myimage= Label(image=Frame_image)


# In[1961]:


frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


# The above code loads an image file of a box frame, creates a label with the frame image, and packs the label onto a tkinter window or frame with 5 pixels of padding on each side and aligned to the bottom of the parent widget.

# Time

# In[1962]:


name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)


# In[1963]:


clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


# The above codes create two labels in the GUI window of the weather app. The first label is named "name" and is styled using the Arial font with a size of 15 and bold text. It is positioned at x-coordinate 30 and y-coordinate 100. The second label is named "clock" and is styled using the Helvetica font with a size of 20. It is positioned at x-coordinate 30 and y-coordinate 130.

# Label

# In[1964]:


label1 = Label(root,text='WIND',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')


# In[1965]:


label1.place(x=120,y=400)


# In[1966]:


label2 = Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')


# In[1967]:


label2.place(x=250,y=400)


# In[1968]:


label3 = Label(root,text='DESCRIPTION',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')


# In[1969]:


label3.place(x=430,y=400)


# In[1970]:


label4 = Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')


# In[1971]:


label4.place(x=650,y=400)


# The above codes creates a label with the text 'WIND', using the font 'Helvetica' with size 15 and bold weight. The label has a foreground color of white and a background color of '#1ab5ef', and is placed at position (120, 400) on a tkinter window or frame and the same for the corresponding codes

# In[1972]:


t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)


# In[1973]:


c = Label(font=('arial',15,"bold"))
c.place(x=400,y=250)


# The above lines of code create two labels in the GUI window of the weather app. The first label is named "t" and is styled using the Arial font with a size of 70 and bold text. It also has a foreground color set to #ee666d. It is positioned at x-coordinate 400 and y-coordinate 150. The second label is named "c" and is styled using the Arial font with a size of 15 and bold text. It is positioned at x-coordinate 400 and y-coordinate 250.

# In[1974]:


w = Label(text="...",font=('arial',20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)


# In[1975]:


h = Label(text="...",font=('arial',20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)


# In[1976]:


d = Label(text="...",font=('arial',20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)


# In[1977]:


p = Label(text="...",font=('arial',20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


# The above lines of code create four labels w, h, d, and p, which display weather information such as wind speed, humidity, description, and pressure respectively. They are placed on the graphical user interface (GUI) window at specific positions (x and y coordinates). The font and background color of each label are also specified.

# In[1978]:


root.mainloop()


# root.mainloop() is a method in Tkinter library which runs the main event loop of the application, waiting for events to occur and responding to them.

# In[ ]:




