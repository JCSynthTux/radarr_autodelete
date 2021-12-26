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

def should_movie_delete(movie, currentTime, keeptime):
    added = movie['added']
    unifiedAdded = added.split('T', 1)[0]
    dateAddedToDatetime = datetime.strptime(unifiedAdded, '%Y-%m-%d')
    dateAddedInSeconds = int(dateAddedToDatetime.timestamp())
    savedTime = currentTime - dateAddedInSeconds
    if savedTime >= keepTime:
        return True
    else:
        return False

def daysToSeconds(numberOfDays):
    days = int(numberOfDays)
    return days * 24 * 60 * 60

load_dotenv()

host_url = os.getenv('RADARR_HOST');

api_key = os.getenv('RADARR_APIKEY');

radarr = RadarrAPI(host_url, api_key);

movies = radarr.get_movie();

dt = datetime.today() 
secondsNow = int(dt.timestamp()) # Now In Seconds
keepTime = daysToSeconds(10) # Time To Keep Movies before Deleting
print(keepTime)
print(secondsNow)
for movie in movies:
    tagged_status = is_movie_tagged(movie, 'theaterslist')
    if tagged_status == True:
        deletable = should_movie_delete(movie, secondsNow, keepTime)
        if deletable == True:
            print('Delete')

