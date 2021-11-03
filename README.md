# Putusan Pilkada Mahkamah Agung Indonesia DataScraper


Program ini digunakan untuk scraping data di website [https://putusan3.mahkamahagung.go.id/search.html](https://putusan3.mahkamahagung.go.id/search.html)

Silahkan digunakan / dicopy / dimodifikasi agar menjadi bermanfaat.


![scraping1](./img/1.png)

![scraping2](./img/2.png)

## Usage
```
usage: putusan-ma.py [-h] -p PAGE [-o FILE_NAME] [-he] [-sp STARTPAGE] [-ep LAST_PAGE] [-sd] [-v]

Putusan Mahkamah Agung Scraper

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        Masukkan keyword pencarian putusan mahkamah agung
```

## How to use
```
git clone https://github.com/okkymabruri/putusan-mahkamahagung
cd putusan-mahkamahagung/
pip install -r requirements.txt
python putusan-ma.py -k "korupsi"
```

Tested di Ubuntu 21.10