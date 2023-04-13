import pandas as pd


# After getting how to grow information using the scrape fucntion and saving as an array in xlsx, I realized that formatting
# could not be parsed by the Wix Content manager. This is code to take a txt file with a bunch of arrays of growing information, including their headers,
# then sort that information by their headers using a dictionary. Name key was needed to reassociate the formatted dictionary info with the relevant category.
# Data was exported to xlsx for ease of use by community partner/for wix import. 

file = open("..\data\\htg.txt", "r", encoding="utf8")
htg_content = file.read()

htg_list = htg_content.split("\n")

htg_arr = [[]]

headers = [" Timing", " Starting", " Growing", " Harvest"]

for item in htg_list:
    htg_arr.append(item.split("', '"))

htg_dict = {'Name': [], 'Timing': [], 'Starting': [], 'Growing': [], 'Harvest': []}

def makeDictEntry(string, entry):
    j = i+1
    while((j<len(entry)) and (entry[j] not in headers)):
        string = string + entry[j]
        j+=1
    return string

for entry in htg_arr:
    i = 0
    timing = ""
    starting = ""
    growing = ""
    harvest = ""
    name = ""
    while i < len(entry):
        if(i == 0):
            name = entry[i]
        if(entry[i] == ' Timing'):
            timing = makeDictEntry(timing, entry)
        if(entry[i] == ' Starting'):
            starting = makeDictEntry(starting, entry)
        if(entry[i] == ' Growing'):
            growing = makeDictEntry(growing, entry)
        if(entry[i] == ' Harvest'):
            harvest = makeDictEntry(harvest, entry)
        i+=1
    htg_dict["Name"].append(name)
    htg_dict["Timing"].append(timing)
    htg_dict["Starting"].append(starting)
    htg_dict["Growing"].append(growing)
    htg_dict["Harvest"].append(harvest)

htg_df = pd.DataFrame.from_dict(htg_dict)

htg_df.to_excel("..\data\\howtogrow.xlsx", sheet_name="htg")



# f_htg = open("..\data\\htg_str.txt", "w")

# f_htg.write(*htg_arr, sep="\n")