import scrape
from scrape import Seed

test = scrape.scrape("https://www.westcoastseeds.com/products/french-lavender")

Seed.printSeed(test)