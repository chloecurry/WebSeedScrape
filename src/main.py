import navigate
import scrape
from scrape import Seed as SeedObj
#have list of names of seeds
#navigate to all pages
    #return page content
#scrape all pages 
    #return seed object
#seed object -> excel spreadsheet/csv
    #return excel spreadsheet/csv\

#seedList = ["Touchstone Gold", "Bull\'s Blood Organic", "Get Stuffed!", "Helenor (Coated) Certified Organic", "TFM", "Tres Fine Maraichere", "TFM (Tres Fine Maraichere)"]
seedList = ["Touchstone Gold", "Bull\'s Blood Organic"]

seedData = []

nav_results = navigate.navigate(seedList)

for seedUrl in nav_results.get("found"):
    seedData.append(scrape.scrape(seedUrl))

