import csv
import json

def _convert():
    infile = open("Twitter_data_userlevel.json","r")
    outfile = open("Twitter_data_userlevel.csv","w")
    writer = csv.writer(outfile)
    for row in json.loads(infile.read()):
        writer.writerow()

if __name__ == '__main__':
    _convert()


