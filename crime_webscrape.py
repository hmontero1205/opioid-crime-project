import urllib.request
from bs4 import BeautifulSoup

crimes_committed = dict()
search_city = "Birmingham"
search_state = "Alabama"

url = "http://www.city-data.com/crime/crime-" + search_city + "-" + search_state + ".html"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
table = soup.find(id="crimeTab")            
tds = table.find_all('td')


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

print(crimes_committed)