import navigate
import scrape
from scrape import Seed as SeedObj
import pandas as pd
import re


# file = open("..\data\seeds.txt", "r")
# seed_txt = file.read()

# seed_txt_list = seed_txt.split("\n")
# seed_list = []

# for seed in seed_txt_list:
#     split1 = re.split(r"- ", seed)[1]
#     spl_seed = re.split(r" \(?\d", split1)[0]
#     seed_list.append(spl_seed)


# seedData = []

# nav_results = navigate.navigate(seed_list)

# foundUrls = list(dict.fromkeys(nav_results.get("found")))
# notFoundUrls = list(dict.fromkeys(nav_results.get("notFound")))

# #create files with url and not found data (easier to run scrape later if changing fields)
# f_url = open("..\data\seedURLS.txt", "w")
# f_nf = open("..\data\\notFound.txt", "w")

# f_url.write('\n'.join(foundUrls))

# f_nf.write('\n'.join(notFoundUrls))

file = open("..\data\\nfSeedURL.txt", "r")
seed_url = file.read()

seed_url_list = seed_url.split("\n")

seedData = []

for seedUrl in seed_url_list:
    seedData.append(SeedObj.seed_to_df(scrape.scrape(seedUrl)))

seed_df = pd.DataFrame(seedData, columns= ["Name", "Latin", "Matures", "Season", "Exposure", "Difficulty", "How to Grow"])

seed_df.to_excel("..\data\\seed_data_missing2.xlsx", sheet_name="missing")