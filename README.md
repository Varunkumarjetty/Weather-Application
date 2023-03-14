# Weather-Application
![1st](https://user-images.githubusercontent.com/119765379/225028784-3c821b78-d368-40c0-8143-b044cf7fc5e8.png)

This weather app built using Python retrieves real-time weather information based on user input, displaying current temperature, weather conditions, and other details in a user-friendly interface.

Various Python libraries used in the weather app are as follows:

tkinter - a standard GUI (Graphical User Interface) library for Python, which provides several widgets like buttons, labels, and text boxes for building graphical interfaces for desktop applications.

requests - an HTTP library that allows you to send HTTP/1.1 requests using Python, which we have used to fetch weather data from the OpenWeatherMap API.

json - a built-in Python library that allows you to work with JSON (JavaScript Object Notation) data, which is a lightweight data interchange format used to exchange data between different programming languages.

pytz - a Python library that allows accurate and cross-platform timezone calculations, which we have used to convert the UTC time returned by the OpenWeatherMap API to local time.

geopy - a Python library that provides several geocoding APIs to find the latitude and longitude of a location based on its name or address, which we have used to get the location of the city entered by the user.

timezonefinder - a lightweight Python library that provides fast and accurate timezone calculations based on latitude and longitude coordinates.

OpenWeatherMap API - an API (Application Programming Interface) that provides current weather data, hourly forecasts, and daily forecasts for cities around the world. We have used this API to fetch the current weather data for the city entered by the user.

This is a user-friendly Weather App created using Python programming language. The app provides real-time weather information of any city across the globe. The GUI of the app is created using the tkinter library, making it easy to use and interactive. The app uses multiple libraries such as requests, pytz, timezonefinder, geopy, and OpenWeatherMap API for fetching and displaying weather information.

Features:

Fetches real-time weather information for any city
Displays temperature, condition, wind, pressure, humidity, and description
Automatically detects the user's time zone and displays local time
User-friendly GUI created using tkinter library

Installation:

Clone the repository or download the zip file
Install the required libraries using pip (requests, pytz, timezonefinder, geopy, tkinter)
Run the weather_app.py file

Usage:

Enter the name of the city for which you want to check the weather
Click on the "Get Weather" button
The app will display the current weather information for the entered city



