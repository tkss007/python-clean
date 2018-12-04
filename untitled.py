import csv
import pandas as pd

data = pd.read_csv('AssocRule13NGC.csv')

"""
for i in range (0,344):
	for j in range(1,2193):
		if (data.ix[i,[j]] is not '0') or (data.ix[i,[j]] is not '1'):
			data.ix[i,[j]] = 'Null'
"""


data = data.fillna(value = 'Null')
"""
print data.ix[4,[4]]
print data.ix[0,[1]]
"""
print data

data.to_csv('out.csv')

#print data.columns.size
#print data.iloc[:,0].size
