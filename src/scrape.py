from lxml import html
import requests

class Seed:
    def __init__(self, name, matures, season, exposure, difficulty, timing, starting, growing, harvest):
        self.name = name
        self.matures = matures
        self.season = season
        self.exposure = exposure
        self.difficulty = difficulty
        self.timing = timing
        self.starting = starting
        self.growing = growing
        self.harvest = harvest

    def printSeed(self):
        print("name: %s \nmatures: %s \nseason: %s \nexposure: %s \ndifficulty: %s \ntiming: %s \nstarting: %s \ngrowing: %s \nharvest: %s"
         % (self.name, self.matures, self.season, self.exposure, self.difficulty, self.timing, self.starting, self.growing, self.harvest))

def scrape(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)

    #name of variety
    name = tree.xpath('//*[@id="shopify-section-product"]/div[1]/div/div[2]/div[1]/h1/text()')
    #print("name: ", name)

    #details, not including title
    details = tree.xpath('/html/body/main/div[2]/div/div[1]/div/div[2]/div[3]//p/text()')
    #print("\ndetails: ", details )

    #all about panel 1 info from accordion panels, not includig title
    allAboutPanel1 = tree.xpath("/html/body/main/div[3]/div/div/div/div[1]//p/text()")
    #print("\n", allAboutPanel1)

    return Seed(name=name[0], exposure = details[1], matures = details[3], season = details[5], difficulty = allAboutPanel1[0],
    timing = allAboutPanel1[1], starting = allAboutPanel1[2], growing = allAboutPanel1[4], harvest = allAboutPanel1[5])
