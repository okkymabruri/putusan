# Putusan Pilkada Mahkamah Agung Indonesia DataScraper


Program ini digunakan untuk scraping data pelanggaran pilkada di website [https://putusan3.mahkamahagung.go.id/search.html?q=pilkada](https://putusan3.mahkamahagung.go.id/search.html?q=pilkada)

Silahkan digunakan / dicopy / dimodifikasi agar menjadi bermanfaat.

Tested di Ubuntu 20.04


![scraping1](https://github.com/okkymabruri/putusan-pilkada-scraping/raw/master/image/1.png)

![scraping2](https://github.com/okkymabruri/putusan-pilkada-scraping/raw/master/image/2.png)

## Prerequisites

#### Update dan Install Package
```
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
```
#### Install Oracle Java 8
```
sudo apt-get install default-jdk
```
#### Install Google Chrome
```
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```
#### Instalasi Chrome Driver
```
wget https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
#### Install Selenium
```
pip install selenium
```

## Menjalankan Program
```
git clone https://github.com/okkymabruri/putusan-pilkada-scraping.git
cd putusan-pilkada-scraping/
pip install -r requirements.txt
python3 scraping.py
```

## Catatan
* Tidak disarankan memakai selenium, kecepatannya lambat
* Jika memakai selenium, sangat direkomendasikan menggunakan google chrome

## Next Project
* Coba pake Scrapy

## Sumber
Thanks to:

* https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
* https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab
* [Perhimpunan Pengembangan Media Nusantara](https://ppmn.or.id/)
