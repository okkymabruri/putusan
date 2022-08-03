# Putusan Mahkamah Agung / Supreme Court Data Scraper


This code is used for scraping data on the website: [https://putusan3.mahkamahagung.go.id/search.html](https://putusan3.mahkamahagung.go.id/search.html)

Feel free to copy/modify.


![scraping1](./img/1.png)

![scraping2](./img/2.png)

## Usage
```
usage: putusan-ma.py [-h] [-k KEYWORD] [-u URL] [-sd] [-dp]

Putusan Mahkamah Agung Scraper

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        keyword for the Supreme Court
  -u URL, --url URL     specify url for the Supreme Court example: https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56
  -sd, --sortdate       (optional) scraping from newest putusan. Default False
  -dp, --downloadpdf    (optional) download pdf. Default False
```

## How to use
```
git clone https://github.com/okkymabruri/putusan-mahkamahagung
cd putusan-mahkamahagung/
pip install -r requirements.txt
python putusan-ma.py -k "korupsi"
```

Tested on Python 3.9.13 and Ubuntu 22.04