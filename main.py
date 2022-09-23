from bs4 import BeautifulSoup
import requests
import cfscrape
import unicodedata
import json
import threading
import re


address_list, page_list, filtered_list = [], [], []

def checkAddress_Launtel():
    while address_list:
        address = address_list[0]
        address_list.remove(address)
        street = address.split(", ")
        street = street[0]

        suburb = re.search(',(.*)VIC', address)
        suburb = suburb.group(1)

        adjusted_address = street + suburb

        if '/' in adjusted_address:
            adjusted_address = adjusted_address[adjusted_address.find('/'):].replace('/','') # Unit can impact the result
        #print(address)

        try:
            nbn_url = 'https://residential.launtel.net.au/search_address'
            post_data = {'term': adjusted_address}
            
            nbn_req = requests.post(nbn_url, data = post_data)
            resp = json.loads(nbn_req.text)

            label = str(resp[0]['label'])
            label = label.split(" - ")

            launtel_address = label[0]
            internet_type = label[1]
            print(launtel_address + ' - ' + internet_type)
            if 'FTTP' in internet_type:
                filtered_list.append(address)
        except:
            print("Error - " + address)

def main():
    my_url = "https://www.domain.com.au/rent/?suburb=clayton-vic-3168,noble-park-vic-3174,clayton-south-vic-3169,springvale-vic-3171,glen-waverley-vic-3150"

    scraper = cfscrape.create_scraper()
    req = scraper.get(my_url).content
    soup = BeautifulSoup(req, "lxml")

    

    for pages in soup.find_all(attrs={'data-testid': 'paginator-page-button'}):
        page_list.append(pages.text.strip())

    print(page_list)

    for page in page_list:
        page_url = my_url + "&page=" + page
        page_req = scraper.get(page_url).content
        page_soup = BeautifulSoup(page_req, "lxml")
        for address_wrap in page_soup.find_all(attrs={'data-testid': 'address-wrapper'}):
            address = unicodedata.normalize("NFKD", address_wrap.text.strip())
            address_list.append(address)


    print(address_list)

    # creating thread
    t1 = threading.Thread(target=checkAddress_Launtel)
    t2 = threading.Thread(target=checkAddress_Launtel)
    t3 = threading.Thread(target=checkAddress_Launtel)
    t4 = threading.Thread(target=checkAddress_Launtel)
    t5 = threading.Thread(target=checkAddress_Launtel)
    t6 = threading.Thread(target=checkAddress_Launtel)
    t7 = threading.Thread(target=checkAddress_Launtel)
    t8 = threading.Thread(target=checkAddress_Launtel)
 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
 
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    res = json.dumps(filtered_list)
    print(res)

if __name__ == '__main__':
    main()