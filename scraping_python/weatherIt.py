import webbrowser

weatherReport = [
    "https://www.accuweather.com/en/id/bandung/208977/weather-forecast/208977",
    "https://www.accuweather.com/en/id/banjarmasin/209036/weather-forecast/209036",
    "https://www.accuweather.com/en/sg/singapore/300597/weather-forecast/300597"
]

for weather in weatherReport:
    webbrowser.open_new(weather)
    