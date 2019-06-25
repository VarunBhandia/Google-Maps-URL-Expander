import requests
import csv
import string
import random


# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
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
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('[#] %s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

# Generate random file name
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
# Expansion of short URL 
def expand_url(file_name):
    print("[#] Updating the URLs")

    file_name = 'Input/' + file_name
    output_file_name = 'Output/'+id_generator() + '.csv'

    f = open(file_name)
    l = len(f.readlines()) -1
    

    with open(file_name,'r') as csvinput:
        with open(output_file_name, 'w') as csvoutput:

            writer = csv.writer(csvoutput, lineterminator='\n')
            reader = csv.reader(csvinput)
            all = []
            row_header = next(reader)
            row_header.append('Updated Location')
            all.append(row_header)
            i =0

            printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            for row in reader:
                i = i+1
                printProgressBar(i+1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

                if(len(row[0]) <= 38 and row[0][0:5] == "https"):
                    r = requests.get(row[0])
                    updated_url = r.url
                    row.append(updated_url)
                else:
                    updated_url = row[0]
                    row.append(updated_url)
                all.append(row)

            writer.writerows(all)

            print("[#] Check the file with name",output_file_name)
    return all

file_name = input("Enter your File Name : ") 

expand_url(file_name)
