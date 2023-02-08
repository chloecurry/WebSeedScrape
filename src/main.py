import navigate
import scrape
from scrape import Seed as SeedObj
import pandas as pd
import re


file = open("..\data\seeds.txt", "r")
seed_txt = file.read()

seed_txt_list = seed_txt.split("\n")
seed_list = []

for seed in seed_txt_list:
    spl_seed = re.split(r" \(?\d", re.split(r"- ", seed)[1])[0]
    seed_list.append(spl_seed)


seedData = []

nav_results = navigate.navigate(seed_list)

foundUrls = list(dict.fromkeys(nav_results.get("found")))

#create files with url and not found data (easier to run scrape later if changing fields)
f_url = open("..\data\seedURLS.txt", "w")
f_nf = open("..\data\\notFound.txt", "w")

f_url.write(foundUrls)

f_nf.write(nav_results.get("notFound"))

for seedUrl in foundUrls:
    seedData.append(SeedObj.seed_to_df(scrape.scrape(seedUrl)))

seed_df = pd.DataFrame(seedData, columns= ["Name", "Matures", "Season", "Exposure", "Difficulty", "How to Grow"])

seed_df.to_excel("seed_data.xlsx", sheet_name="test")