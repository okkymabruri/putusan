#!/usr/bin/env python

# Importing packages
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
import pandas as pd

driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')

print(driver.title)

link = []
for i in range(1, 22):
    link.append('/html/body/div[1]/section/div/div/section/div/div[2]/div[' +  str(i) + '3]/div/strong/a')

for i in range(1, 3):
    putusan = 'https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page='
    driver.get(putusan + str(i))
    linkopen = []
    for i in range(21):
        items = driver.find_elements_by_xpath(link[i])
        for item in items:
            href = item.get_attribute('href')
        print(href)

        #print(a)
        #linkopen.append(a.href)
        #print(linkopen[i])


    driver.get('https://putusan3.mahkamahagung.go.id/direktori/putusan/06c05c2759b6926fab71e70047d407a1.html')


data = pd.DataFrame(columns=[
    'Nomor',
    'ParaPihak',
    'TingkatProses',
    'Klasifikasi',
    'Tahun',
    'TanggalRegister',
    'LembagaPeradilan',
    'JenisLembagaPeradilan',
    'HakimKetua',
    'HakimAnggota',
    'Panitera',
    'Amar',
    'CatatanAmar',
    'TanggalMusyawarah',
    'TanggalDibacakan',
    'Kaidah',
    'Status'])

Xpath = '/html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/'

Nomor = driver.find_elements_by_xpath(Xpath + 'tr[1]/td[2]')[0].text
ParaPihak = driver.find_elements_by_xpath(Xpath + 'tr[2]/td[2]')[0].text
TingkatProses = driver.find_elements_by_xpath(Xpath + 'tr[3]/td[2]')[0].text
Klasifikasi = driver.find_elements_by_xpath(Xpath + 'tr[4]/td[2]')[0].text
Tahun = driver.find_elements_by_xpath(Xpath + 'tr[5]/td[2]')[0].text
TanggalRegister = driver.find_elements_by_xpath(Xpath + 'tr[6]/td[2]')[0].text
LembagaPeradilan = driver.find_elements_by_xpath(Xpath + 'tr[7]/td[2]')[0].text
JenisLembagaPeradilan = driver.find_elements_by_xpath(Xpath + 'tr[8]/td[2]')[0].text
HakimKetua = driver.find_elements_by_xpath(Xpath + 'tr[9]/td[2]')[0].text
HakimAnggota = driver.find_elements_by_xpath(Xpath + 'tr[10]/td[2]')[0].text
Panitera = driver.find_elements_by_xpath(Xpath + 'tr[11]/td[2]')[0].text
Amar = driver.find_elements_by_xpath(Xpath + 'tr[12]/td[2]')[0].text
CatatanAmar = driver.find_elements_by_xpath(Xpath + 'tr[13]/td[2]')[0].text
TanggalMusyawarah = driver.find_elements_by_xpath(Xpath + 'tr[14]/td[2]')[0].text
TanggalDibacakan = driver.find_elements_by_xpath(Xpath + 'tr[15]/td[2]')[0].text
Kaidah = driver.find_elements_by_xpath(Xpath + 'tr[16]/td[2]')[0].text
Status = driver.find_elements_by_xpath(Xpath + 'tr[17]/td[2]')[0].text

data = data.append({
    'Nomor': Nomor,
    'ParaPihak': ParaPihak,
    'TingkatProses': TingkatProses,
    'Klasifikasi': Klasifikasi,
    'Tahun': Tahun,
    'TanggalRegister': TanggalRegister,
    'LembagaPeradilan': LembagaPeradilan,
    'JenisLembagaPeradilan': JenisLembagaPeradilan,
    'HakimKetua': HakimKetua,
    'HakimAnggota': HakimAnggota,
    'Panitera': Panitera,
    'Amar': Amar,
    'CatatanAmar': CatatanAmar,
    'TanggalMusyawarah': TanggalMusyawarah,
    'TanggalDibacakan': TanggalDibacakan,
    'Kaidah': Kaidah,
    'Status': Status}, ignore_index=True)

print(data)
data.to_excel("output.xlsx")

driver.quit()