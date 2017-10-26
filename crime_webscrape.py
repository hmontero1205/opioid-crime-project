import urllib.request
from bs4 import BeautifulSoup

def extract_data(search_city, search_state):
    crimes_committed = dict()
    
    url = "http://www.city-data.com/crime/crime-" + search_city + "-" + search_state + ".html"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    
    #Data table
    table = soup.find(id="crimeTab")            
    tds = table.find_all('td')
    
    
    #Extract data from crime stats website. 
    for cell in tds:
        if ".com" in str(cell.contents[0]):
            break
        
        if "N/A" in str(cell.contents[0]):
            continue
        
        if "<b>" in str(cell.contents[0]):
            header = str(cell.contents[0].contents[0])
        else:
            num_committed = int(str(cell.contents[0].replace(",", "")))
            if not(header in crimes_committed.keys()):
                crimes_committed[header] = 0
            
            crimes_committed[header] += num_committed
            
    #Easily accessible data stored in a dictionary
    return crimes_committed

#Test Code
print(extract_data("New-York", "New-York"))