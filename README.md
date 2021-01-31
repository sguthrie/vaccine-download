# vaccine-download
Pull information from MA government vaccine website and format into CSV

## Installing and Running
This project uses [poetry](https://python-poetry.org/docs/) as a package manager. Once it's installed, run the following to install dependencies in a poetry
virtual environment:

```
poetry install
```

In order to update to AirTable, scrape_and_upload looks at the environment variable
`AIRTABLE_API_TOKEN`. You should export your api token to this environment variable
before running the script.


Use `poetry run` command to run the script.

```
poetry run python scrape_and_upload.py -h

usage: scrape_and_upload.py [-h] [--ma-url MA_URL] [--link-match-checks LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...]]
                            [--airtable AIRTABLE_BASE AIRTABLE_TABLE_NAME] [--airtable-unique-key-name AIRTABLE_UNIQUE_KEY_NAME]

Pull Vaccine Site Info from MA and push to AirTable

optional arguments:
  -h, --help            show this help message and exit
  --ma-url MA_URL       Site to scrape. Defaults to https://www.mass.gov/info-details/covid-19-vaccine-locations-for-individuals-
                        in-phase-1#find-a-location-to-get-vaccinated-if-eligible-
  --link-match-checks LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...], -l LINK_MATCH_CHECKS [LINK_MATCH_CHECKS ...]
                        Strings to match against the title of the link to search for. Defaults to ["download"] (Capitalization
                        does not matter)
  --airtable AIRTABLE_BASE AIRTABLE_TABLE_NAME
                        Airtable to upload to. Defaults to ('appA95GVaCrTcCMxQ', 'Table 1')
  --airtable-unique-key-name AIRTABLE_UNIQUE_KEY_NAME
                        Airtable to upload to. Defaults to "Location Name"
```
