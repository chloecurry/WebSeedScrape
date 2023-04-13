import navigate
import scrape
from scrape import Seed as SeedObj
import pandas as pd
import re

# Initial code used for getting seed information from the west coast seeds website. Utilizes scrape and navigate functions.
# Content was exported to xlsx for ease of use by community partners.

# Read seed names from text file
file = open("..\data\seed_names.txt", "r")
seed_txt = file.read()

seed_list = seed_txt.split("\n")

#retrieve URLs (this step will take a while)
nav_results = navigate.navigate(seed_list)

foundUrls = list(dict.fromkeys(nav_results.get("found")))
notFoundUrls = list(dict.fromkeys(nav_results.get("notFound")))

#create files with url and not found data (easier to run scrape later if changing fields)
f_url = open("..\data\seedURLS.txt", "w")

f_url.write('\n'.join(foundUrls))

file = open("..\data\\SeedURLS.txt", "r")
seed_url = file.read()

seed_url_list = seed_url.split("\n")

#Get seed information from all URLs found using navigate
seedData = []

for seedUrl in seed_url_list:
    seedData.append(SeedObj.seed_to_df(scrape.scrape(seedUrl)))

#Store information in a DataFrame for easy export to xlsx
seed_df = pd.DataFrame(seedData, columns= ["Name", "Latin", "Matures", "Season", "Exposure", "Difficulty", "How to Grow"])

seed_df.to_excel("..\data\\seed_data.xlsx", sheet_name="seeds")