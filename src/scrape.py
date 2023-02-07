from lxml import html
import requests

class Seed:
    def __init__(self, name, matures, season, exposure, difficulty, htg):
        self.name = name
        self.matures = matures
        self.season = season
        self.exposure = exposure
        self.difficulty = difficulty
        self.htg = htg

    def printSeed(self):
        print("name: %s \nmatures: %s \nseason: %s \nexposure: %s \ndifficulty: %s \nhow to grow: %s"
         % (self.name, self.matures, self.season, self.exposure, self.difficulty, self.htg))
    
    def seed_to_df(self):
        return [self.name, self.matures, self.season, self.exposure, self.difficulty, self.htg]

def scrape(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    #name of variety
    name = tree.xpath('//h1[@class="header-font-secondary"]/text()')
    #print("name: ", name)

    #details & title
    exposure = ""
    matures = ""
    season = ""
    details = tree.xpath('//div[@class="product-facts"]//span/text() | //div[@class="product-facts"]//p/text()')
    for id, entry in enumerate(details):
        entry = entry.strip()
        if(entry == "Exposure"):
            exposure = details[id+1].strip()
        elif(entry == "Season"):
            season = details[id+1].strip()
        elif(entry == "Matures"):
            matures = details[id+1].strip()

    #all about panel 1 info from accordion panels, not includig title
    aap = tree.xpath('//div[@id = "all-about"]//strong/text() | //div[@id = "all-about"]//p/text()')
    for id, entry in enumerate(aap):
        if(entry == "Difficulty"):
            if(aap[id+1] != "Difficulty"):
                difficulty = aap[id+1].strip()

    htgContent = tree.xpath('//div[@class="content-section how-to-grow"]//div[@class="htg-text"]//h4/text() | //div[@class="content-section how-to-grow"]//div[@class="htg-text"]//p/text()')

    return Seed(name=name[0], exposure = exposure, matures = matures, season = season, difficulty = difficulty, htg = htgContent)