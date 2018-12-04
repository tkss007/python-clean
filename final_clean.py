import csv
from datetime import datetime, date
import datetime

csv_reader=open("VET_Export_clean.csv","r")

with open("after_clean.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['VehicleModel','SerialNumber','TestName','Status','Weekofday'])

result = []

#print datetime.datetime.now().weekday()

lines = csv_reader.readlines()
csv_reader.close()



for line in lines:
    #print line
    n = line.count(',')
    VehicleModel = line.split(',')[0]
    SerialNumber = line.split(',')[1]
    TestName = line.split(',')[2]
    TestName.replace('"','')
    TestName.replace('"','')
    Status = line.split(',')[3]
    loc = line.split(',')[4]
    Date = line.split(',')[5]
    date = Date[11:]
    #print date[:4],date[5:7],date[8:]
   
    #print type(weekofday)
    if n > 5:
        TestName = line.split(',')[2] + line.split(',')[3]
        TestName.replace('"','')
        TestName.replace('"','')
        Status = line.split(',')[4]
        loc = line.split(',')[5]
        Date = line.split(',')[6]
        date = Date[11:]
    print date
    Status.strip('\r\n')

    #print VehicleModel, SerialNumber,TestName,Status
#print [TestName]
#print (Status)
#   print type(VehicleModel)


    if VehicleModel == 'NGC':
        if loc == '013':

            #if result == []:
            result = [[VehicleModel] + [SerialNumber] + [TestName] + [Status] + [date]]
#print result
            with open("after_clean.csv","a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(result)
                result = []
                #print type(result[0][1])
        """    elif result[0][1] == SerialNumber:
                result[0] = result[0] + [TestName]
                result[0] = result[0] + [Status]
                #print SerialNumber
            elif result[0][1] != SerialNumber:"""




