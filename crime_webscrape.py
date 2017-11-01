#Hans Montero & Rhys Murray

import urllib
from bs4 import BeautifulSoup


def extract_crime_data(search_city, search_state):
    crimes_committed = dict()
    
    url = "http://www.city-data.com/crime/crime-" + search_city + "-" + search_state + ".html"
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return crimes_committed
    soup = BeautifulSoup(page, "html.parser")
    
    #Data table
    table = soup.find(id="crimeTab")  
    year_list = list()     
    for th in table.findAll("th"):
        cell_data = str(th.contents[0].contents[0])
        if cell_data != "Type":
            year_list.append(cell_data)
    tds = table.find_all('td')

    #Extract data from crime stats website. 
    year_idx = 0
    for cell in tds:
        if ".com" in str(cell.contents[0]):
            break
        
        if "N/A" in str(cell.contents[0]):
            continue
        
        if "<b>" in str(cell.contents[0]):
            header = str(cell.contents[0].contents[0])
            year_idx = 0
        else:
            if year_list[year_idx] == "2016":
                continue
            
            num_committed = int(str(cell.contents[0].replace(",", "")))
            if not(header in crimes_committed.keys()):
                crimes_committed[header] = dict()
            
            crimes_committed[header][year_list[year_idx]] = num_committed
            year_idx += 1
            
    #Easily accessible data stored in a dictionary
    
    return crimes_committed

def county_code_to_cities(cc):
    global fz_dict
    cities_found = set()
    for zip_code in fz_dict[cc]:
        url = ("https://www.searchbug.com/tools/zip-code-lookup.aspx?TYPE=zip2city&ZIP=" + zip_code)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        cities_found.add(tuple(str(soup.findAll("font")[2].contents[0]).strip().split(", ")))
    return(cities_found)

def zip_to_cities(zip_code):
    cities_found = set()
    url = ("https://www.searchbug.com/tools/zip-code-lookup.aspx?TYPE=zip2city&ZIP=" + zip_code)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    cities_found.add(tuple(str(soup.findAll("font")[2].contents[0]).strip().split(", ")))
    return(cities_found)
    
    
def read_county_to_zip():
    fips_to_zips = open("county_to_zip.csv","r", encoding = 'utf-8')
    fz_dict = dict()
    for line in fips_to_zips:
        line_info = line.strip().split("\t")
        c_fips = line_info[0]
        c_zip = line_info[1]
        if len(c_zip) == 4:
            c_zip = "0" + c_zip
        
        if not(c_fips in fz_dict.keys()):
            fz_dict[c_fips] = set()
        fz_dict[c_fips].add(c_zip)
        
    return(fz_dict)
    
def counties_to_crimes(cc):
    crime_dict = dict()
    for city in county_code_to_cities(cc):
        city_name = city[0].replace(" ", "-").title()
        state_name = city[1].replace(" ", "-").title()
        crime_dict[city] = extract_crime_data(city_name, state_name)
    
    print(crime_dict)
fz_dict = read_county_to_zip()
#zip_to_cities("11385")














#Test Code
#crime_hash = extract_crime_data("New-York", "New-York")
#print(crime_hash)

counties_to_crimes("53077")

"""objects = tuple(crime_hash.keys())
y_pos = np.arange(len(objects))
performance = crime_hash.values()
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number committed since 2002')
plt.title('Crime')
 
#plt.show()
"""

#Returns {'Murders': 7204, 'Rapes': 21014,'Robberies': 316217, 'Assaults': 441340,
#'Burglaries': 302784, 'Thefts': 1745775, 'Auto thefts': 199297}
