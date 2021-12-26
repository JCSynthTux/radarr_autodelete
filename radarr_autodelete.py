import os
from datetime import datetime
from dotenv import load_dotenv
from pyarr import RadarrAPI

def is_movie_tagged(movie, filtertag):
    tags = movie['tags']
    if tags != []:
        for tag in tags:
            texttag = radarr.get_tag(tag)
            if texttag['label'] == filtertag:
                return True
    else:
        return False

def should_movie_delete(movie, currentTime):
    added = movie['added']
    unifiedAdded = added.split('T', 1)[0]
    dateAddedToDatetime = datetime.strptime(unifiedAdded, '%Y-%m-%d')
    dateAddedInSeconds = int(dateAddedToDatetime.timestamp())
    print(dateAddedInSeconds)

load_dotenv()

host_url = os.getenv('RADARR_HOST');

api_key = os.getenv('RADARR_APIKEY');

radarr = RadarrAPI(host_url, api_key);

movies = radarr.get_movie();


dt = datetime.today() 
secondsNow = int(dt.timestamp())
print(secondsNow)
for movie in movies:
    tagged_status = is_movie_tagged(movie, 'theaterslist')
    if tagged_status == True:
        deletable = should_movie_delete(movie, secondsNow)

