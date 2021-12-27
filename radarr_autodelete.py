import os
from argparse import ArgumentParser
from datetime import datetime
from dotenv import load_dotenv
from pyarr import RadarrAPI

def is_movie_tagged(movie, filtertag): # Function Checks Movies For A Specific Tag
    tags = movie['tags']
    if tags != []:
        for tag in tags:
            texttag = radarr.get_tag(tag)
            if texttag['label'] == filtertag:
                return True
    else:
        return False

def should_movie_delete(movie, currentTime, keeptime): # Function validates if a movie should be deleted
    added = movie['added']
    unifiedAdded = added.split('T', 1)[0]
    dateAddedToDatetime = datetime.strptime(unifiedAdded, '%Y-%m-%d')
    dateAddedInSeconds = int(dateAddedToDatetime.timestamp())
    savedTime = currentTime - dateAddedInSeconds
    if savedTime >= keeptime:
        return True
    else:
        return False

def daysToSeconds(numberOfDays): # Function Converts Days To Seconds
    days = int(numberOfDays)
    return days * 24 * 60 * 60

load_dotenv()

parser = ArgumentParser()
parser.add_argument('--keeptime', help='Time To Keep Movies In Days', default=30)
parser.add_argument('--filtertag', help='Tag To Filter For')
parser.add_argument('--dryrun', help='Use this to see what results would look like, without loosing data', default=False)
args = parser.parse_args()

host_url = os.getenv('RADARR_HOST');

api_key = os.getenv('RADARR_APIKEY');

radarr = RadarrAPI(host_url, api_key);

movies = radarr.get_movie();

dt = datetime.today() 
secondsNow = int(dt.timestamp()) # Now In Seconds
keepTime = daysToSeconds(int(args.keeptime)) # Time To Keep Movies before Deleting
filtertag = args.filtertag
dryrun = bool(args.dryrun)

if dryrun == True:
    print('THIS IS A DRYRUN')

for movie in movies:
    tagged_status = is_movie_tagged(movie, filtertag)
    if tagged_status == True:
        deletable = should_movie_delete(movie, secondsNow, keepTime)
        if deletable == True:
            if dryrun == True:
              print('Deleting ' + movie['title'])
            else: 
              print('Deleting ' + movie['title'])
              radarr.del_movie(movie['id'], True)
