import csv


with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column1 = [row['SerialNumber'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column2 = [row['TestSessionID'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column3 = [row['TestId'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column4 = [row['TestName'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column5 = [row['VehicleModel'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column6 = [row['TesterID'] for row in reader]
    
with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column7 = [row['Status'] for row in reader]

with open("VET_Export_1000.csv","r") as f:
    reader = csv.DictReader(f)
    column8 = [row['loc'] for row in reader]


rows = zip(column1,column2,column3,column4,column5,column6,column7,column8)

with open("VET_Export_1000_clean.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['SerialNumber','TestSessionID','TestId','TestName','VehicleModel','TesterID','Status','loc'])
    for row in rows:
        writer.writerow(row)
