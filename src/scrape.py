from lxml import html
import requests

page = requests.get("https://www.westcoastseeds.com/products/pink-brandywine-organic")
tree = html.fromstring(page.content)
print(tree.xpath)

#name of variety
name = tree.xpath('//*[@id="shopify-section-product"]/div[1]/div/div[2]/div[1]/h1/text()')
print("name: ", name)

#details, not including title
details = tree.xpath('/html/body/main/div[2]/div/div[1]/div/div[2]/div[3]//p/text()')
print("\ndetails: ", details )

#all about panel 1 info from accordion panels, not includig title
allAboutPanel1 = tree.xpath("/html/body/main/div[3]/div/div/div/div[1]//p/text()")
print("\n", allAboutPanel1)
#https://www.westcoastseeds.com/collections/tomato-seeds

#https://www.westcoastseeds.com/products/pink-brandywine-organic