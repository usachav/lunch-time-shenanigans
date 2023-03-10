import csv


url = ("https://www.mscdirect.com/product/details/")

filename = '/home/frankd/Desktop/numbers.csv'
with open(filename) as f:
    reader = csv.reader(f)
    id = next(reader)
    print(id)
    
for x in id:
    print(url + str(x))