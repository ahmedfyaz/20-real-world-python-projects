import  requests
import selectorlib
from  emailing import send_email
import  time
import  sqlite3


"INSERT INTO events VALUES('Tigers','Tiger City','2088.10.14')"
"SELECT* FROM events WHERE data = '2088.10.14'"
"DELETE FROM events WHERE name = 'Lions'"
connection = sqlite3.connect('data.db')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL  = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """SCRAPE THE PAGE SOURCE FROM URL"""
    response = requests.get(url,headers=HEADERS)
    source = response.text
    return  source
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value



def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT* FROM events WHERE band = ? AND city = ? AND date = ?",(band,city,date))
    row = cursor.fetchall()
    return row

if  __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        read(extracted)
        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(extracted)
        time.sleep(2)



