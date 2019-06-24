import requests
import pandas as pd
import pprint

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

def expand_url(urls):
    expanded_url_list = []
    print("Reading the File")
    dfe = pd.read_csv(file_name)
    urls = list(dfe['Location'])
    print("Expanding the URLs")
    f = open("nihit_ki_bandi.txt", "w")
    count =0 
    length = len(urls)
    printProgressBar(0, length, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for url in urls:
        count =count +1
        printProgressBar(count, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        if(len(url) <= 38 and url[0:5] == "https"):
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
