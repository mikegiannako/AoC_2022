import requests
from datetime import date
from requests import Response
import os
import json

# We get the date automatically from the datetime module
day_today : int = int(date.today().strftime("%d").lstrip("0"))

# Get year from date module
year : int = int(date.today().strftime("%Y").lstrip("0"))

# Load the 'cookies.json' file WHICH SHOULD BE IN THE SAME DIRECTORY (if you keep
# the path the same as this code) and return the value of the 'cookie_name' key
def load_cookie(cookie_name : str) -> str:
    with open("cookies.json", "r") as f:
        return json.load(f)[cookie_name]

URL : str = f"https://adventofcode.com/{year}/day/{day_today}/input"

# Requests the input from the website and returns the response. The cookie session
# has to be added to the requests headers so that the website knows who we are
# A cookie session lasts about a month, so you don't have to worry about it expiring
r : Response = requests.get(URL, cookies = {'session': load_cookie('advent_cookie')})

# Then what I do is I make a new folder for each day
os.mkdir(f"Day{day_today}")

os.rename("tools/parsing.py", f"Day{day_today}/parsing.py")

# Then I move into that folder
os.chdir(f"Day{day_today}")

# Then we create a new file for the input and write the response to it
with open(f"input{day_today}.txt","w+") as f:
    f.write(r.text)

# Then we create a new file for the solution and write the boilerplate code to it
with open(f"solution{day_today}.py","w+") as f:
    f.write(f'''from parsing import *

# Problem link: {URL}

def part1():
    count = 0

def part2():
    count = 0

if __name__ == "__main__":
    print(part1())
    #print(part2())
''')