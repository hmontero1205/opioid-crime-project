#Hans Montero & Rhys Murray
import crime_webscrape as c
import FileReader as o
import pylab 
def findCrime(zc):
    #returns a dictionary of crimes for a given zipcode
    cities = c.zip_to_cities(zc)
    if cities is None:
        return list()
    
    crime_dict = dict()
    for city in cities:
        city_name = city[0].replace(" ", "-").title()
        state_name = city[1].replace(" ", "-").title()
        crime_dict[city] = c.extract_crime_data(city_name, state_name)
    return crime_dict
def plotCrimeData(zc):
    #takes a zipcode and plots the crime in that zipcode
    crimes = findCrime(zc)
    if crimes is None or len(crimes) == 0:
        return False
    pylab.figure()
    atLeastOne = False
    for CityTuple, value in crimes.items():
        cityName = CityTuple[0]
        pylab.title("Crimes in " + str(cityName))
        for CrimeName, allYears in value.items():
            atLeastOne = True
            pylab.plot(list(allYears.keys()), list(allYears.values()), label=CrimeName)
    if not(atLeastOne):
        return False
    pylab.ylabel("Rate per 100,000 residents")
    pylab.xlabel("Year")
    pylab.legend(loc='upper left')
    pylab.savefig('images/crimes.png')
    return True
def zip_to_county(zc):
    #returns county code for a given zipcode
    countyCode = 0
    for fips_code, zips in c.fz_dict.items():
        for zip_code in zips:
            if zip_code == zc:
                countyCode = fips_code
    return countyCode
def plotOpioidData(zc):
    #plots the opioid deaths for a given zipcode
    pylab.figure()
    cc = zip_to_county(zc)
    cities = c.zip_to_cities(zc)
    if cities is None or len(cities) == 0:
        return False
    cityList = list()
    for city in cities:
        cityList.append(city)
    if len(cityList) == 1:
        cityName = cityList[0][0]
    else:
        return False
    cc = int(cc)
    selectedDeaths = o.deathsDict[cc]
    pylab.title("Deaths due to Opioids in " + str(cityName))
    pylab.plot(list(selectedDeaths.keys()), list(selectedDeaths.values()))
    pylab.ylabel("Crude Death rate per 100,000 residents")
    pylab.xlabel("Year")
    pylab.savefig('images/deaths.png')
    return True