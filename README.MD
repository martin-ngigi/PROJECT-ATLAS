## PROJECT ATLAS
- Create requirements text file
```
pip freeze > requirements.txt
```

- install requirements.txt
```
pip install -r requirements.txt
```
or
```
pip install -r /path/to/requirements.txt
```

- Create Admin
```
python manage.py createsuperuser
```
- Sample Admin credentials
```
username: admin
email: admin@gmail.com
password: 123456
```

- Create App
```
python manage.py startapp application
```

- Activate virtaul Enviroment in Windows
```
.venv\scripts\activate
```
- Activate virtaul Enviroment in Mac
```
source .venv/bin/activate
```


- Run server
```
python manage.py runserver
```

- Make migrations
```
python manage.py makemigrations
```
- Run migrations
```
python manage.py migrate
```

## Climate Data APIS:
- World Banks (Documentation)[https://climateknowledgeportal.worldbank.org/download-data]
- https://pypi.org/project/wbpy/
- (National Center for Environmental Information)[https://www.ncei.noaa.gov/cdo-web/webservices/v2]

## Free weather APIs
```
Visual Crossing	
Tomorrow.io	
Weatherbit
Weatherstack
AccuWeather
```

- Confirm table exists:
```
python manage.py dbshell
.tables  -- (if SQLite)
\dt      -- (if Postgres)
show tables; -- (if MySQL)
```

- Certificate issue:
```
open "/Applications/Python 3.13/Install Certificates.command"
```
- Python Version: 
```
Python 3.14.0
```
| Climate Type (Enum)      | Measurement Unit | Unit Standardized           | Open-Meteo Daily URL                                                                                                                                                                                                                                                                                                                           | NASA POWER Daily URL                                                                                                                                                                                                                                                                                                                                 |
| ------------------------ | ---------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TEMPERATURE**          | °C               | Celsius                     | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=temperature_2m_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=temperature_2m_mean&timezone=auto)                 | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                             |
| **PRECIPITATION**        | mm               | Millimeters                 | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=precipitation_sum&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=precipitation_sum&timezone=auto)                     | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)             |
| **HUMIDITY**             | %                | Percentage                  | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=relative_humidity_2m_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=relative_humidity_2m_mean&timezone=auto)     | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=RH2M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=RH2M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                           |
| **WIND_SPEED**           | m/s              | Meters per second           | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=wind_speed_10m_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=wind_speed_10m_mean&timezone=auto)                 | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=WS10M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=WS10M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                         |
| **WIND_DIRECTION**       | °                | Degrees                     | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=wind_direction_10m_dominant&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=wind_direction_10m_dominant&timezone=auto) | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=WD10M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=WD10M&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                         |
| **ATMOSPHERIC_PRESSURE** | hPa              | Hectopascals                | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=pressure_msl_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=pressure_msl_mean&timezone=auto)                     | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PS&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PS&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                               |
| **CLOUD_COVER**          | %                | Percentage                  | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=cloud_cover_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=cloud_cover_mean&timezone=auto)                       | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=CLOUD_AMT&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=CLOUD_AMT&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                 |
| **SOLAR_RADIATION**      | MJ/m²            | Megajoules per square meter | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=shortwave_radiation_sum&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=shortwave_radiation_sum&timezone=auto)         | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_SW_DWN&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON) |
| **DEW_POINT**            | °C               | Celsius                     | [https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=dew_point_2m_mean&timezone=auto](https://archive-api.open-meteo.com/v1/archive?latitude=1.75&longitude=40.05&start_date=2024-01-01&end_date=2024-12-31&daily=dew_point_2m_mean&timezone=auto)                     | [https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2MDEW&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON](https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2MDEW&community=AG&longitude=40.0573&latitude=1.7471&start=20240101&end=20241231&format=JSON)                       |
