#!/usr/bin/env python

# Importing packages
from selenium import webdriver

options = webdriver.ChromeOptions()
# options = webdriver.FirefoxOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
import pandas as pd
import time

driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Firefox(firefox_options=options, executable_path='/usr/local/bin/geckodriver')
driver.delete_all_cookies()

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
    'Status',
    'Laman'])


def safe_execute(function):
    value = []
    getvalue = []
    while True:
        try:
            value = function
            getvalue = value[0].text
            return getvalue
        except IndexError:
            pass
        return getvalue


link = []
for z in range(1, 23):
    link.append('//section/div/div[2]/div[' + str(z) + ']/div/strong/a')
    # link.append('//*[@id="content"]/div/div[2]/div[' + str(z) + ']/div/strong/a')
for i in range(1, 138):
    putusan = 'https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page='
    driver.get(putusan + str(i))

    url = []
    for j in range(22):
        items = driver.find_elements_by_xpath(link[j])

        for item in items:
            href = item.get_attribute('href')
            url.append(href)
    print('Halaman ' + str(i))

    for k in range(len(url)):
        driver.get(url[k])
        time.sleep(1)
        # Xpath = '/html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/'
        Xpath = '//*[@id="popular-post-list-sidebar"]/ul/table/tbody/'

        Nomor = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[1]/td[2]'))
        ParaPihak = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[2]/td[2]'))
        TingkatProses = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[3]/td[2]'))
        Klasifikasi = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[4]/td[2]'))
        Tahun = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[5]/td[2]'))
        TanggalRegister = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[6]/td[2]'))
        LembagaPeradilan = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[7]/td[2]'))
        JenisLembagaPeradilan = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[8]/td[2]'))
        HakimKetua = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[9]/td[2]'))
        HakimAnggota = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[10]/td[2]'))
        Panitera = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[11]/td[2]'))
        Amar = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[12]/td[2]'))
        CatatanAmar = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[13]/td[2]'))
        TanggalMusyawarah = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[14]/td[2]'))
        TanggalDibacakan = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[15]/td[2]'))
        Kaidah = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[16]/td[2]'))
        Status = safe_execute(driver.find_elements_by_xpath(Xpath + 'tr[17]/td[2]'))
        Laman = url[k]

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
            'Status': Status,
            'Laman': Laman}, ignore_index=True)

    print(data)
    data.to_excel("output.xlsx")
driver.quit()
