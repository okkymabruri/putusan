#!/usr/bin/env python

#Importing packages
from selenium import webdriver
import pandas as pd

# https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page=1
# ...
# https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page=137

# html(/body/div[1]/section/div/div/section/div/div[2]/div[1]/div/strong/a)
# ...
# html(/body/div[1]/section/div/div/section/div/div[2]/div[22]/div/strong/a)


driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://putusan3.mahkamahagung.go.id/direktori/putusan/06c05c2759b6926fab71e70047d407a1.html')

Xpath = '/html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/'
Nomor =  driver.find_elements_by_xpath(Xpath + 'tr[1]/td[2]')[0].text
ParaPihak =  driver.find_elements_by_xpath(Xpath + 'tr[2]/td[2]')[0].text
TingkatProses =  driver.find_elements_by_xpath(Xpath + 'tr[3]/td[2]')[0].text
Klasifikasi =  driver.find_elements_by_xpath(Xpath + 'tr[4]/td[2]')[0].text
Tahun =  driver.find_elements_by_xpath(Xpath + 'tr[5]/td[2]')[0].text
TanggalRegister =  driver.find_elements_by_xpath(Xpath + 'tr[6]/td[2]')[0].text
LembagaPeradilan =  driver.find_elements_by_xpath(Xpath + 'tr[7]/td[2]')[0].text
JenisLembagaPeradilan =  driver.find_elements_by_xpath(Xpath + 'tr[8]/td[2]')[0].text
HakimKetua =  driver.find_elements_by_xpath(Xpath + 'tr[9]/td[2]')[0].text
HakimAnggota =  driver.find_elements_by_xpath(Xpath + 'tr[10]/td[2]')[0].text
Panitera =  driver.find_elements_by_xpath(Xpath + 'tr[11]/td[2]')[0].text
Amar =  driver.find_elements_by_xpath(Xpath + 'tr[12]/td[2]')[0].text
CatatanAmar =  driver.find_elements_by_xpath(Xpath + 'tr[13]/td[2]')[0].text
TanggalMusyawarah =  driver.find_elements_by_xpath(Xpath + 'tr[14]/td[2]')[0].text
TanggalDibacakan =  driver.find_elements_by_xpath(Xpath + 'tr[15]/td[2]')[0].text
Kaidah =  driver.find_elements_by_xpath(Xpath + 'tr[16]/td[2]')[0].text
Status =  driver.find_elements_by_xpath(Xpath + 'tr[17]/td[2]')[0].text
