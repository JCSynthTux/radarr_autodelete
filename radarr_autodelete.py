import os
from argparse import ArgumentParser
from datetime import datetime
from tabnanny import verbose
from dotenv import load_dotenv
from pyarr import RadarrAPI

def is_movie_tagged(movie, filtertag): # Function Checks Movies For A Specific Tag
    tags = movie['tags']
    if tags != []: # Checks if tag array is not empty
        for tag in tags: # Iterate over tags
            texttag = radarr.get_tag(tag) # Get HumanReadable Tags
            if texttag['label'] == filtertag: # If HumanReadable Tag matches Specified Filter Tag return True
                return True
    else: # If there are no tags return False
        return False

def should_movie_delete(movie, currentTime, keeptime): # Function validates if a movie should be deleted
    if 'movieFile' in movie:
        moviefileObj = movie['movieFile']
        added = moviefileObj['dateAdded']
        unifiedAdded = added.split('T', 1)[0]
        dateAddedToDatetime = datetime.strptime(unifiedAdded, '%Y-%m-%d')
        dateAddedInSeconds = int(dateAddedToDatetime.timestamp())
        savedTime = currentTime - dateAddedInSeconds
        if savedTime >= keeptime: return True
        else: return False
    else : return False

def daysToSeconds(numberOfDays): # Function Converts Days To Seconds
    days = int(numberOfDays)
    return days * 24 * 60 * 60

load_dotenv()

parser = ArgumentParser()
parser.add_argument('--keeptime', help='Time To Keep Movies In Days', default=30)
parser.add_argument('--filtertag', help='Tag To Filter For')
parser.add_argument('--dryrun', help='Use this to see what results would look like, without loosing data', action='store_true')
parser.add_argument('--verbose', help='Outputs movies deleted', action='store_true')
args = parser.parse_args()

host_url = os.getenv('RADARR_HOST')

api_key = os.getenv('RADARR_APIKEY')

radarr = RadarrAPI(host_url, api_key)

movies = radarr.get_movie()

dt = datetime.today() 
secondsNow = int(dt.timestamp()) # Now In Seconds
keepTime = daysToSeconds(int(args.keeptime)) # Time To Keep Movies before Deleting
filtertag = args.filtertag
dryrun = bool(args.dryrun)

print('#### ' + dt.strftime("%m/%d/%Y, %H:%M:%S") + ' ####')

if dryrun:
    print('----THIS IS A DRYRUN----')

print('----RADARR_AUTODELETE----')
print('KEEPTIME: ' + str(args.keeptime))
print('FILTERTAG: ' + filtertag)

for movie in movies:
    tagged_status = is_movie_tagged(movie, filtertag)
    if tagged_status:
        deletable = should_movie_delete(movie, secondsNow, keepTime)
        if deletable:
            if dryrun | args.verbose:
              print('Deleting ' + movie['title'])
            if dryrun == False:
              radarr.del_movie(movie['id'], True)
              
print('#### FINISHED ###')