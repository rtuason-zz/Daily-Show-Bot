from data_import import fetch_guest_list
from flask import Flask

from dateutil import parser as dateparser
from collections import defaultdict
import re

guest_list = fetch_guest_list()
application = Flask(__name__)

BASE_WIKI_URL = 'https://en.wikipedia.org/wiki/'
MIN_YEAR = 1999
MAX_YEAR = 2015

######################################################################
# Data transformation helper functions
######################################################################
def is_valid_year(input):
  year_format = re.compile("\d{4}")
  return year_format.match(input) and int(input) >= MIN_YEAR and int(input) <= MAX_YEAR

def get_appearance_dates(target_guest):
  results = []
  for guest_info in guest_list:
    if guest_info['Raw_Guest_List'].lower() == target_guest.lower():
      results.append(guest_info['Show'])
  return results

def get_groups():
  results = set()
  for guest_info in guest_list:
    results.add(guest_info['Group'].title())
  return sorted(results)


######################################################################
# Response construction helper functions
######################################################################
def create_guest_from_date_resp(date, name, occupation, all_dates):
  output = "{name} appeared on The Daily Show on {date} and is known to be a(n) {occupation}.<br>".format(
    name=name,
    date=date,
    occupation=occupation
  )

  if len(all_dates) > 1:
    other_dates = [curr_date for curr_date in all_dates if curr_date != date]
    output += "This person has also appeared on the following dates:<br>{dates}<br>".format(
      name=name,
      dates="<br>".join(other_dates)
    )
  else:
    output += "This person has not made another appearance on the show.<br>".format(name=name)

  output += create_wiki_link(name)

  return output

def create_dates_from_guest_resp(name, all_dates):
  name = name.title()

  if all_dates:
    output = "{name} appeared on The Daily Show on the following dates:<br>{all_dates}<br>".format(
      name=name.title(),
      all_dates="<br>".join(all_dates)
    )
    output += create_wiki_link(name)
  else:
    output = "{name} has not made an appearance on The Daily Show.<br>".format(name=name)

  return output

def create_invalid_group_resp(group, all_groups):
  output = "'{group}' is not in our list of groups. Valid options are limited to:<br>{all_groups}".format(
    group=group.lower(),
    all_groups="<br>".join(all_groups)
  )
  return output

def create_invalid_year_resp():
  output = "Please input a year between {MIN_YEAR} and {MAX_YEAR}, inclusive.".format(
    MIN_YEAR=MIN_YEAR,
    MAX_YEAR=MAX_YEAR
  )
  return output

def create_wiki_link(name):
  wiki_url = BASE_WIKI_URL + name
  output = "Learn more about {name} at <a href='{wiki_url}'>{wiki_url}</a>.<br>".format(
    name=name,
    wiki_url=wiki_url
  )
  return output


######################################################################
# Primary Flask functions
######################################################################
@application.route('/date/<date>')
def get_guest_from_date(date):
  try:
    target_date = dateparser.parse(date)
  except:
    return "Invalid date provided"

  for guest_info in guest_list:
    curr_date = dateparser.parse(guest_info['Show'])
    if curr_date == target_date and guest_info['Group'] != 'NA':
      name = guest_info['Raw_Guest_List']
      occupation = guest_info['GoogleKnowlege_Occupation'].lower()
      all_dates = get_appearance_dates(name)
      return create_guest_from_date_resp(guest_info['Show'], name, occupation, all_dates)

  return "No guest appeared on " + date

@application.route('/name/<name>')
def get_dates_from_guest(name):
  all_dates = get_appearance_dates(name)
  return create_dates_from_guest_resp(name, all_dates)
  
@application.route('/group/<group>')
def get_most_popular_in_group(group):
  all_groups = get_groups()

  if group.title() not in all_groups:
    return create_invalid_group_resp(group, all_groups)
  else:
    guests = defaultdict(int)
    for guest_info in guest_list:
      if group.lower() == guest_info['Group'].lower():
        guests[guest_info['Raw_Guest_List']] += 1

    num_picks = min(5, len(guests))

    top_guests = sorted(guests, key=guests.get, reverse=True)[:num_picks]
    top_guests = ["{guest} ({num_times}) ({wiki_link})".format(
      guest=guest,
      num_times=guests[guest],
      wiki_link="<a href='{link}'>{link}</a>".format(link=BASE_WIKI_URL + guest)
    ) for guest in top_guests]

    output = "Within the '{group}' group, the following guests appeared the most:<br>{top_guests}<br>".format(
      group=group.lower(),
      top_guests="<br>".join(top_guests)
    )
    return output

@application.route('/year-groups/<year>')
def get_groups_by_year(year):
  if not is_valid_year(year):
    return create_invalid_year_resp()
  else:
    groups = defaultdict(int)
    for guest_info in guest_list:
      if year == guest_info['YEAR']:
        groups[guest_info['Group'].title()] += 1
    total = sum(groups.values())

    groups = sorted(groups.items(), key=lambda x: x[1], reverse=True)

    output = "In {year}, guests from the following groups appeared: <br>".format(year=year)
    for group, value in groups:
      output += "{group} : {percentage}%<br>".format(
        group=group,
        percentage=str(round(value / total * 100, 2))
      )

    return output

@application.route('/year-group-guests/<year>/<group>')
def get_guests_by_year_group(year, group):
  all_groups = get_groups()

  if not is_valid_year(year):
    return create_invalid_year_resp()
  elif group.title() not in all_groups:
    return create_invalid_group_resp(group, all_groups)
  else:
    results = []
    for guest_info in guest_list:
      if group.lower() == guest_info['Group'].lower() and year == guest_info['YEAR']:
        results.append(guest_info)

    if results:
      output = "In {year}, the following guests from the '{group}' group appeared on The Daily Show:<br>".format(
        year=year,
        group=group.lower()
      )
      for guest_info in results:
        output += "{name} ({date}) ({wiki_link})<br>".format(
          name=guest_info['Raw_Guest_List'],
          date=guest_info['Show'],
          wiki_link="<a href='{link}'>{link}</a>".format(link=BASE_WIKI_URL + guest_info['Raw_Guest_List'])
        )
    else:
      output = "In {year}, no guests from the '{group}' group appeared on The Daily Show<br>".format(
        year=year,
        group=group.lower()
      )

    return output


if __name__ == '__main__':
  application.run(debug=True, use_reloader=True)