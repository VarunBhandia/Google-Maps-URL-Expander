import requests
import pandas as pd
import pprint

def expand_url(urls):
    expanded_url_list = []
    print("Reading the File")
    dfe = pd.read_csv(file_name)
    urls = list(dfe['Location'])
    print("Expanding the URLs")
    f = open("nihit_ki_bandi.txt", "w")
    count =0 
    length = len(urls)
    for url in urls:
        count =count +1
        percentage_completed = (count * 100)/length 
        print(round(percentage_completed), '% completed')
        if(len(url) == 37):
            r = requests.get(url)
            expanded_url_list.append(r.url)
        else:
            expanded_url_list.append(url)

    for expanded_url in expanded_url_list:
        f.write(expanded_url)
        f.write("\n")
    print("You can now fuck Nihit ki bandi.")
    f.close()

    return expanded_url_list

file_name = 'sexy.csv'
expand_url(file_name)
