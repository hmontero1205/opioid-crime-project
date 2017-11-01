import pandas as pd
import collections
def readTable():
    dataTable = pd.read_table("/Users/rhysmurray/Desktop/Opioid Project/Opiod Deaths by County 1999-2015.txt")
    dataTable = dataTable[dataTable.notnull()]
    CrudeDeathRate_Years_CountyCode = dataTable[["County Code", "Year", "Crude Rate", "Population"]]
    DeathRateDict = collections.defaultdict(dict)
    for index, row in CrudeDeathRate_Years_CountyCode.iterrows():
        if row['Population'] == "Unreliable" or row['Population'] == 'Missing':
            row['Population'] =  0
        if float(row['Population']) < 10000:
            CrudeDeathRate_Years_CountyCode = CrudeDeathRate_Years_CountyCode.drop(index)
    for index, row in CrudeDeathRate_Years_CountyCode.iterrows():
        if row['Crude Rate'] == "Unreliable" or row['Crude Rate'] == 'Missing':
            row['Crude Rate'] = 0
        DeathRateDict[row['County Code']][row['Year']] = row['Crude Rate']
    return DeathRateDict
def getHighestValue(n):
    highestValue = 0
    highestValueKey1 = ''
    highestValueKey2 = ''
    for key1, value1 in n.items():
        for key2, value2 in value1.items():
            if float(value2) > highestValue:
                highestValue = float(value2)
                highestValueKey1 = key1
                highestValueKey2 = key2
    return (highestValueKey1, highestValueKey2, highestValue)

    