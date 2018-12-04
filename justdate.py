import csv
from datetime import datetime, date
import datetime

csv_reader=open("VET_Export_clean.csv","r")

with open("after_clean111.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['SerialNumber','Weekofday'])

result = []

#print datetime.datetime.now().weekday()

back = []

lines = csv_reader.readlines()
csv_reader.close()


def DateToWeek(year, month, day):
    if month == 1 or month == 2:
        year -= 1
        month += 12
    return (day + 2 * month + 3 * (month + 1) / 5 + year + year / 4 - year / 100 + year / 400) % 7 + 1


m=0
t=0
w=0
th=0
f=0
sat=0
sun=0


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
    date = Date[:10]
    #print date[:4],date[5:7],date[8:]
    if date[0] == '2':
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        weekofday = DateToWeek(year,month,day)
    #print type(weekofday)
    if n > 5:
        TestName = line.split(',')[2] + line.split(',')[3]
        TestName.replace('"','')
        TestName.replace('"','')
        Status = line.split(',')[4]
        loc = line.split(',')[5]
        Date = line.split(',')[6]
        date = Date[:10]
        if date[0] == '2':
            year = int(date[:4])
            month = int(date[6:7])
            day = int(date[8:])
            weekofday = DateToWeek(year,month,day)
    Status.strip('\r\n')

    #print VehicleModel, SerialNumber,TestName,Status
#print [TestName]
#print (Status)
#   print type(VehicleModel)


    if VehicleModel == 'NGC':
        if loc == '013':
            if weekofday not in [1,2,3,4,5,6,7]:
                print "hahahah"
            if weekofday == 1:
                m = m + 1
            if weekofday == 2:
                t = t + 1
            if weekofday == 3:
                w = w + 1
            if weekofday == 4:
                th = th + 1
            if weekofday == 5:
                f = f + 1
            if weekofday == 6:
                sat = sat + 1
            if weekofday == 7:
                sun = sun + 1

            if SerialNumber not in back:
                result = [[SerialNumber] + [weekofday]]
                back = back + [SerialNumber]
                print SerialNumber
#print result
            with open("after_clean111.csv","a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(result)
                result = []
                #print type(result[0][1])
        """    elif result[0][1] == SerialNumber:
                result[0] = result[0] + [TestName]
                result[0] = result[0] + [Status]
                #print SerialNumber
            elif result[0][1] != SerialNumber:"""


#result = []
print m,t,w,th,f,sat,sun



