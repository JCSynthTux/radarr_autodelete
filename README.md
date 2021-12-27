# radarr_autodelete
Simple script, which deletes movies with a specific tag after a certain amount of days

# Pip Packages

1. pyarr
2. dotenv

# Running
python3 radarr_autodelete.py --keeptime 30 --filtertag theaterslist

The keeptime arguments only expects full days and defaults to 30 days. filtertag has to be provided
