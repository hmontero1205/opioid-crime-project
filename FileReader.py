#Hans Montero & Rhys Murray
import pandas as pd
import collections
def readTable():
    dataFile = open('assets/Opioid_Deaths_by County_1999-2015.txt',"r")
    dataTable = pd.read_table(dataFile)
    dataTable = dataTable[dataTable.notnull()]
    CrudeDeathRate_Years_CountyCode = dataTable[["County Code", "Year", "Crude Rate", "Population"]]
    DeathRateDict = collections.defaultdict(dict)
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
            if float(value2) > highestValue and key1 != 12017:
                highestValue = float(value2)
                highestValueKey1 = key1
                highestValueKey2 = key2
    return (highestValueKey1, highestValueKey2, highestValue)
def getLowestValue(n):
    lowestValue = 1000
    lowestValueKey1 = ''
    lowestValueKey2 = ''
    for key1, value1 in n.items():
        for key2, value2 in value1.items():
            if float(value2) < lowestValue and value2 != 0:
                lowestValue = float(value2)
                lowestValueKey1 = key1
                lowestValueKey2 = key2
    return (lowestValueKey1, lowestValueKey2, lowestValue)
deathsDict = readTable()

