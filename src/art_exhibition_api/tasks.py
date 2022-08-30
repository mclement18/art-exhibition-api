from .scheduler import scheduler
from .services.exhibition_service import ExhibitionService
from .services.weather_service import WeatherService
from .db import all_exhibitions, replace_exhibitions

@scheduler.task("cron", id="download_exhibition", coalesce=True, max_instances=1, day="*", hour="8")
def download_exhibitions():
    with scheduler.app.app_context():
        exhibition_service = ExhibitionService(scheduler.app.config['HARVARD_MUSEUM_API_KEY'])
        exhibitions = exhibition_service.call()
        replace_exhibitions(exhibitions)

@scheduler.task("interval", id="get_forcast", coalesce=True, max_instances=1, hours=2, misfire_grace_time=900)
def get_forcast():
    with scheduler.app.app_context():
        forcast_service = WeatherService()
        exhibitions = all_exhibitions()
        exhibitions = [forcast_service.call(exhibition) for exhibition in exhibitions]
        replace_exhibitions(exhibitions)

def first_task():
    download_exhibitions()
    get_forcast()
