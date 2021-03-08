# Putusan Pilkada Mahkamah Agung Indonesia DataScraper


Program ini digunakan untuk scraping data di website [https://putusan3.mahkamahagung.go.id/search.html](https://putusan3.mahkamahagung.go.id/search.html)

Silahkan digunakan / dicopy / dimodifikasi agar menjadi bermanfaat.

Tested di Ubuntu 20.10


![scraping1](./img/1.png)

![scraping2](./img/2.png)

## Demo
![scraping2](./img/demo.gif)

## Prerequisites

## Menjalankan Program
```
git clone https://github.com/okkymabruri/putusan-mahkamahagung
cd putusan-mahkamahagung/
pip install -r requirements.txt
python putusan-ma.py -p https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56 -o putusanUUITE
```

## Sumber
Thanks to:

* https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
* https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab
* [Perhimpunan Pengembangan Media Nusantara](https://ppmn.or.id/)
