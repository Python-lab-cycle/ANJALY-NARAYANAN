import csv
csv_col=['ID','Name','Place']
dict_data=[{'ID':1,'Name':'Alex','Place':'Paingottor'},
           {'ID':2,'Name':'Anjaly','Place':'kadavoor'},
           {'ID':3,'Name':'Akhila','Place':'Paimattam'},
           {'ID':4,'Name':'Aparnna','Place':'Cheruvattor'},
           {'ID':5,'Name':'Nivya','Place':'Muvattupzha'},
           {'ID':6,'Name':'Ramsina','Place':'Nerimangalam'},
           {'ID':7,'Name':'Jilta','Place':'kothamangalam'}]
try:
    with open("Names.csv",'w')as file1:
        writer1=csv.DictWriter(file1,fieldnames=csv_col)
        writer1.writeheader()
        for data1 in dict_data:
            writer1.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
                   
