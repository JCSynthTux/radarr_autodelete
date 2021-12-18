import os
from dotenv import load_dotenv
from pyarr import RadarrAPI

def is_movie_tagged(movie, filtertag):
    tags = movie['tags']
    if tags != []:
        print('Found Tagged Movie: ' + movie['title'])
        for tag in tags:
            texttag = radarr.get_tag(tag)
            if texttag['label'] == filtertag:
                return True
    else:
        return False

load_dotenv()

host_url = os.getenv('RADARR_HOST');

api_key = os.getenv('RADARR_APIKEY');

radarr = RadarrAPI(host_url, api_key);

movies = radarr.get_movie();

for movie in movies:
    result = is_movie_tagged(movie, 'theaterslist')
    if result == True:
        print('movie is tagged')

