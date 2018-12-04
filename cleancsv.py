import csv
"""
with open("data_clean.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['SerialNumber','TestSessionID','TestId','TestName','VehicleModel','TesterID','Status','loc'])"""

with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column1 = [row['SerialNumber'] for row in reader]

with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column4 = [row['TestName'] for row in reader]
    
with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column5 = [row['VehicleModel'] for row in reader]
    
with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column7 = [row['Status'] for row in reader]

with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column8 = [row['loc'] for row in reader]

with open("VET_Export.csv","r") as f:
    reader = csv.DictReader(f)
    column9 = [row['Starttime'] for row in reader]


rows = zip(column5,column1,column4,column7,column8,column9)

with open("VET_Export_clean.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['VehicleModel','SerialNumber','TestName','Status','loc','Time'])
    for row in rows:
        writer.writerow(row)
