# vaccine-download
Pull information from MA government vaccine website and format into CSV

## Installing and Running
This project uses [poetry](https://python-poetry.org/docs/) as a package manager. Once it's installed, run the following to install dependencies in a poetry 
virtual environment:

```
poetry install
```


Use `poetry run` command to run the script.

```
poetry run python scrape_and_download.py -h

usage: scrape_and_download.py [-h] [--url URL] [--outfile [OUTFILE]]
                              [--link-match-checks LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...]]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             Site to scrape. Defaults to https://www.mass.gov/info-details/covid-19-vaccine-locations-for-individuals-
                        in-phase-1#find-a-location-to-get-vaccinated-if-eligible-
  --outfile [OUTFILE], -o [OUTFILE]
                        Filename to write downloaded csv to. Defaults to stdout
  --link-match-checks LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...], -l LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...]
                        Strings to match against the title of the link to search for. Defaults to ["download"] (Capitalization
                        does not matter)
```
