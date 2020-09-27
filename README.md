# putusan-pilkada-scraping


Program ini digunakan untuk scraping data pelanggaran pilkadi di website putusan bla bla

Silahkan digunakan / copy / modifikasi. FREEDOM 0!


## Prerequisites

### Update dan Install Package
```
sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
```

### Install Oracle Java 8

```
sudo apt-get install default-jdk
```

### Install Google Chrome

```
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
```

## Instalasi Chrome Driver

```
wget https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```

## Install Selenium
```
pip install selenium
```

## Run
```
git clone https://github.com/okkymabruri/putusan-pilkada-scraping.git
cd putusan-pilkada-scraping/
python3 scraping.py
```

## Catatan
* Sangat direkomendasikan menggunakan google chrome
* Tidak disarankan memakai selenium, kecepatannya lambat 

## Next Project
* Conver to Scrapy

## Sumber

https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab
