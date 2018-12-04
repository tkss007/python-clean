import csv

Test_Name=open("VET_Export_clean.csv","r")
csv_reader=open("after_clean.csv","r")
"""
with open("after_clean.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(['VehicleModel','SerialNumber','TestName','Status'])

"""
count = 1
################## Write first line ###################
lines = Test_Name.readlines()
Test_Name.close()
   
Names = []

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
        if TestName not in Names:
            Names = Names + [TestName]
    """if len(result) > 50:
                    break"""
with open("test.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow('VehicleModel')
    writer.writerow('SerialNumber')
    writer.writerow(Names)
#print Names
################## Write other things ####################
lines_csv = csv_reader.readlines()
csv_reader.close()


"""data = []
for line in lines_csv:
    VehicleModel = line.split(',')[0]
    SerialNumber = line.split(',')[1]
    data = data + [[VehicleModel] + [SerialNumber]]
    i = 2
    n = len(line)
"""
 
"""
    print line[3]

    while i < (n-2):
        TestName = line.split(',')[2]
        TestName.replace('"',"")
        Status = line.split(',')[3]
        data[0].extend(Status)
        #print i
        i = i + 2

    #print data

    with open("test.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow(data[0])
        data = []
        #i = 0
        count = count + 1
"""


width = 371
result = []
#a = [list() for i in xrange (width)]
#b = range (width + 1)
for i in range (0,width):
    result = result + []
name = []
data = []
dataset = []
for line in lines_csv:
    temp = line
    #data = []
    #i = 2
    #while i:
    x = line.count(',')
    #VehicleModel = line.split(',')[0]
    #SerialNumber = line.split(',')[1]
    #result[0][0] = line.split(',')[0]
    #result[0][1] = line.split(',')[1]
    #print result[0][1]
    #print line.split(',')[1]
    #print ('\n')
    loc = 0
    for i in range(2,x,2):
        name = line.split(',')[i]
        data = line.split(',')[i+1]
        data.replace('"','')
        #i = i + 2
        if name in Names:
            loc = Names.index(name)
            #print loc
            #print data[1]
            #result[loc] = data[1]
            print result[loc], loc, name
            result[loc] = data[1]
    #n = len(line)
    #print result
    with open("test.csv","a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)
        data = []
        
        result = []
        for i in range (0,width):
            result = result + []

