import csv

csv_reader=open("VET_Export_clean.csv","r")


result = ['VehicleModel', 'SerialNumber']


lines = csv_reader.readlines()
csv_reader.close()
    
for line in lines:
    n = line.count(',')
    VehicleModel = line.split(',')[0]
    SerialNumber = line.split(',')[1]
    TestName = line.split(',')[2]
    Status = line.split(',')[3]
    if n > 3:
        TestName = line.split(',')[2] + line.split(',')[3]
        Status = line.split(',')[4]
    #print(VehicleModel, SerialNumber,TestName,Status)
    #print type(VehicleModel)
    if VehicleModel == 'NGC':
        if TestName not in result:
            result = result + [TestName]
    """if len(result) > 50:
                    break"""
with open("TestName.csv","w") as f:
    writer = csv.writer(f)
    #writer.writerow()
    writer.writerow(result)
    
#result = []

