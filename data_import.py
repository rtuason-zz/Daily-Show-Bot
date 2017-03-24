from os import makedirs
from os.path import exists
from os.path import join

import csv
import requests
from dateutil import parser as dateparser

SRC_URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/daily-show-guests/daily_show_guests.csv"
DATA_DIR = 'data'
RAW_FILENAME = "daily_show_guests.csv"

def fetch_guest_list():
  makedirs(DATA_DIR, exist_ok=True)
  filename = join(DATA_DIR, RAW_FILENAME)

  if not exists(filename):
    resp = requests.get(SRC_URL)
    with open(filename, 'wb') as f:
      f.write(resp.content)

  with open(filename, 'r') as f:
    return prepare_guest_list(f)

# List comprehension is pretty damn powerful, albeit harder to read
def prepare_guest_list(f):
  guests = list(csv.DictReader(f))
  guests = [dict(x) for x in set([tuple(guest_info.items()) for guest_info in guests if guest_info['Group'] != 'NA'])]
  return sorted(
    guests,
    key=lambda x: dateparser.parse(x['Show'])
  )