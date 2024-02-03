import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Specify the required weather variables (order is important)
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 37.76,
    "longitude": 122.40,
    "start_date": "2021-01-01",
    "end_date": "2024-01-01",
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,cloudcover,direct_radiation,direct_normal_irradiance,windspeed_10m,winddirection_10m,windgusts_10m,pressure_msl",
    "temperature_unit": "fahrenheit"
}

responses = openmeteo.weather_api(url, params=params)

# Process first location (add a loop for multiple locations or models)
response = responses[0]

# ... (Print coordinates, elevation, timezone information) ...

# Process hourly data
hourly = response.Hourly()

# Extract variables in the correct order
hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s"),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}

variable_names = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "cloudcover",
    "direct_radiation",
    "direct_normal_irradiance",
    "windspeed_10m",
    "winddirection_10m",
    "windgusts_10m",
    "pressure_msl"
]

for i, variable_name in enumerate(variable_names):
    hourly_data[variable_name] = hourly.Variables(i).ValuesAsNumpy()

hourly_dataframe = pd.DataFrame(data=hourly_data)
print(hourly_dataframe)