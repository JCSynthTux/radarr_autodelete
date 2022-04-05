# radarr_autodelete

## About
Simple script, which deletes movies with a specific tag after a certain amount of days

## Running this script

### On host
1. Clone this repo and cd into the cloned dir
2. Run ```pip3 install pyarr python-dotenv```
2. Create a ```.env``` file in the same dir with ```radarr_autodelete.py```
3. Add the following envs to ```.env```
    ```
    RADARR_APIKEY=
    RADARR_HOST=
    ```
4. Add your API Key and Hostname or IP (Hostname and IP have to http:// or https:// before)
5. Run this script with
    ```
    python3 radarr_autodelete.py --keeptime 30 --filtertag NameOfYourList
    ```
### Via Docker
1. Make sure ```docker-compose``` is installed
2. Clone this repo and cd into the cloned dir
3. Create a ```.env``` file in the same dir with ```docker-compose.yml```
4. Add the following envs to ```.env```
    ```
    RADARR_APIKEY=
    RADARR_HOST=
    KEEPTIME=
    FILTERTAG=
    ```
5. Add your API Key, Hostname or IP (Hostname and IP have to http:// or https:// before),tag which should be scanned and how long the movies should be kept before deleting.
6. Run ```docker-compose up -d```

## Arguments
```--keeptime```

The keeptime arguments only expects full days and defaults to 30 days and is optional. 

\
```--filtertag```

This is the tag this script will look for. This means untagged movies or movies with a different tag will not be touched. filtertag has to be provided.

\
```--deleteunavailablemovies```

Without this flag movies will only be removed if the movies has been downloaded 30 days before run. If this flag is set movies will be deleted if they are older than 30 days and have not been downloaded yet. This flag is meant for clean up in cases where a movie cant be found within an expected time frame and quality.

\
```--dryrun```

This is meant to show which movies would be deleted if the flag wasnt set. Omit to delete movies.

\
```--verbose```

Set this flag for a more detailed output.
