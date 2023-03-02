import re


file = open("..\data\seeds.txt", "r")
seed_txt = file.read()

seed_txt_list = seed_txt.split("\n")
seed_list = []

for seed in seed_txt_list:
    split1 = re.split(r"- ", seed)[1]
    spl_seed = re.split(r" \(?\d", split1)[0]
    seed_list.append(spl_seed)



f_seeds = open("..\data\seed_names.txt", "w")


f_seeds.write('\n'.join(seed_list))
