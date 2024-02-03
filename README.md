# Summary
Just found the Open Meteo API and impressed with the amount of historical data available and relative simplicity of the API.  That said, reading Open Meteo's API documentation, I wasn't able to find a good example of how to pull multiple weather variables (temperature, humidity, cloud cover, irradiance, wind speed, etc.) so after some tinkering, here's a working script. NOTE: this script is the pull HISTORICAL data.  if you wish to pull FORECAST data, follow instructions in the API Documentation (see below link).

# How to use
- download the script
- change the Lat Lon in the params (line 13) to the Latitude and Longitude of where you want to pull data for
- change the 'hourly' descriptors to whatever descriptive weather data you want to pull.  full list of hourly params can be found here in the API documentation: https://open-meteo.com/en/docs/historical-weather-api/
- run the script

# Objective
I will be utilizing this data in the near future to forecast aggregate Solar and Wind generation in California.  Coming soon!
