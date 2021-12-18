import os
from dotenv import load_dotenv
from pyarr import RadarrAPI

load_dotenv()

host_url = os.getenv('RADARR_HOST');

api_key = os.getenv('RADARR_APIKEY');

radarr = RadarrAPI(host_url, api_key);
