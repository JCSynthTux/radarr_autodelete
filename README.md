# radarr_autodelete
Simple script, which deletes movies with a specific tag after a certain amount of days

# Pip Packages

```
pip3 install pyarr python-dotenv
```

# Running
1. Clone this repo and cd into the cloned dir
2. Create a ```.env``` file
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

# Arguments
- keeptime
The keeptime arguments only expects full days and defaults to 30 days. 

- filtertag
This is the tag this script will look for. This means untagged movies or movies with a different tag will not be touched. filtertag has to be provided

- dryrun
This is meant to show which movies would be deleted if the flag wasnt set. With this flag set to ```true``` no movies would be deleted. The flag has to be a boolean, so either ```true``` or ```false```. The flag can also be ommited, which is equal to setting this flag to false.
