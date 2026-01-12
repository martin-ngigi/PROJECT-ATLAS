from django.urls import path, include
from .open_meteo.views import OpenMeteoDailyWeatherView, OpenMeteoMonthlyWeatherView, DailyPrecipitationView
from .ncei.views import NCEIDailyWeatherView, NCEIMonthlyWeatherView
from .nasa.views import NASADailyWeatherView, NASAMonthlyWeatherView
from .weather_views import AggregatedWeatherView

urlpatterns = [
    path("open-meto/", include([
        path("daily", OpenMeteoDailyWeatherView.as_view(), name="open_meteo_weather_daily"),
        path("monthly", OpenMeteoMonthlyWeatherView.as_view(), name="open_meteo_weather_monthly9"),
    ])),

    path("ncei/", include([
        path("daily", NCEIDailyWeatherView.as_view(), name="ncei_daily_weather"),
        path("monthly", NCEIMonthlyWeatherView.as_view(), name="ncei_monthly_weather"),
    ])),

    path("nasa/", include([
        path("daily", NASADailyWeatherView.as_view(), name="nasa_daily_weather"),
        path("monthly", NASAMonthlyWeatherView.as_view(), name="nasa_monthly_weather"),
    ])),

    path("aggregate/", include([
        path("monthly", AggregatedWeatherView.as_view(), name="aggregate_monthly_temperature"),
    ])),
]