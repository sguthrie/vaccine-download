import argparse
import io
import os
import requests
import time
import sys

from airtable import Airtable
from bs4 import BeautifulSoup
from collections import defaultdict
from openpyxl import load_workbook

from helpers import get_download_link, get_curr_ma_data, get_curr_airtable_data_and_update_list

DEFAULT_URL = 'https://www.mass.gov/info-details/covid-19-vaccine-locations-for-individuals-in-phase-1#find-a-location-to-get-vaccinated-if-eligible-'

AIRTABLE_BASE = 'appA95GVaCrTcCMxQ'
AIRTABLE_TABLE_NAME = 'Table 1'
AIRTABLE_UNIQUE_VAL = 'Location Name'

parser = argparse.ArgumentParser(description='Pull Vaccine Site Info from MA and push to AirTable')
parser.add_argument(
    '--ma-url',
    nargs=1,
    default=DEFAULT_URL,
    help=f'Site to scrape. Defaults to {DEFAULT_URL}'
)
parser.add_argument(
    '--link-match-checks',
    '-l',
    nargs='+',
    action='extend',
    default=['download'],
    help='Strings to match against the title of the link to search for. Defaults to ["download"] (Capitalization does not matter)'
)
parser.add_argument(
    '--airtable',
    nargs=2,
    default=[AIRTABLE_BASE, AIRTABLE_TABLE_NAME],
    metavar=('AIRTABLE_BASE', 'AIRTABLE_TABLE_NAME'),
    help=f'Airtable to upload to. Defaults to {AIRTABLE_BASE, AIRTABLE_TABLE_NAME}'
)
parser.add_argument(
    '--airtable-unique-key-name',
    nargs=1,
    default=AIRTABLE_UNIQUE_VAL,
    help=f'Airtable to upload to. Defaults to "{AIRTABLE_UNIQUE_VAL}"'
)

args = parser.parse_args()
vaccination_site_url = get_download_link(args.ma_url, args.link_match_checks)
curr_ma_data = get_curr_ma_data(vaccination_site_url, args.airtable_unique_key_name)
table = Airtable(*args.airtable, os.environ['AIRTABLE_API_TOKEN'])
curr_airtable_data, to_update, up_to_date = get_curr_airtable_data_and_update_list(
    table, args.airtable_unique_key_name, curr_ma_data
)

print(f'{len(to_update)} entries to update')
for entry_name in to_update:
    values = {}
    for field in to_update[entry_name]:
        values[field] = curr_ma_data[entry_name][field]
    print(table.update(curr_airtable_data[entry_name]['id'], values))
    time.sleep(table.API_LIMIT)

entries_to_add = []
for entry_name, entry in curr_ma_data.items():
    if entry_name not in to_update and entry_name not in up_to_date:
        entries_to_add.append(entry)

print(f'{len(entries_to_add)} entries to add. {len(up_to_date)} up to date')
print(table.batch_insert(entries_to_add))
