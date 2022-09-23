# NBN-Crawler

## Introduction
For me, internet speed (both download and upload speeds) is one of the main factors in my choice of property, so when I'm looking for properties, those that offer FTTP services are my priority. For example, when I am sifting through properties in the Melbourne CBD, entering addresses one by one to get their NBN service type is a very slow process, which prompted me to write this script.

## Get Started
BeautifulSoup (bs4) is used to better format the code for the requested URLs as well as to more easily select and read the elements in the page, while cfscrape is a simple Python module to bypass Cloudflare's anti-bot page.
```
pip install bs4
pip install cfscrape
```

## Usage
Filter the listings you want in 'Filters' and click 'Search' (as you would for a normal search). When your browser is redirected to a new page, copy the address from the address bar and replace the value of 'my_url'.

```
python main.py
```

Happy FTTP Searching.

### Note
At current stage, you will need to manually adjust the State as I only need data from VIC, so better coding is not written.
Replace VIC with other state abbreviations, if needed.
```
suburb = re.search(',(.*)VIC', address)
```
