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
        url = ("http://www.addresses.com/zip-code-lookup/" + zip_code)
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        city_str = soup.find(id = "ZIP_qloc").attrs['value']
        city_state = city_str[:len(city_str) - 6].split(", ")
        cities_found.add((city_state[0], sa_dict[city_state[1]]))
    return(cities_found)

def zip_to_cities(zip_code):
    global sa_dict
    cities_found = set()
    url = ("http://www.addresses.com/zip-code-lookup/" + zip_code)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    city_str = soup.find(id = "ZIP_qloc").attrs['value']
    city_state = city_str[:len(city_str) - 6].split(", ")
    cities_found.add((city_state[0], sa_dict[city_state[1]]))
    return(cities_found)
def read_county_to_zip():
    fips_to_zips = open("assets/county_to_zip.csv","r", encoding = 'utf-8')
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
def read_state_abbv():
    abbvs_to_states = dict()
    abbv_file = open("assets/states.csv")
    for line in abbv_file:
        info = line.strip().split(",")
        abbvs_to_states[info[0]] = info[1]
    return abbvs_to_states

def counties_to_crimes(cc):
    crime_dict = dict()
    for city in county_code_to_cities(cc):
        city_name = city[0].replace(" ", "-").title()
        state_name = city[1].replace(" ", "-").title()
        crime_dict[city] = extract_crime_data(city_name, state_name)
    
    return crime_dict

"""
Reading in CSV files for webscraping
"""
fz_dict = read_county_to_zip()
sa_dict = read_state_abbv()