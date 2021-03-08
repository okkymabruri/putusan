#!/usr/bin/env python

# Importing packages
from selenium import webdriver # webdriver from selenium framework to load web
import pandas as pd # pandas library fpr data processing
import time # time library to manipulate time (pause, etc)
import datetime

timenow = datetime.datetime.now().strftime("%m-%d-%Y")
# Webdriver setup, you can use Chrome or Firefor
options = webdriver.ChromeOptions()
# options = webdriver.FirefoxOptions()  # if use firefox (firefox fast than chrome but more inconsistency
options.add_argument("disable-infobars") # add option to disable info bar
options.add_argument("--disable-extensions") # add option to disable browser extension
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver') # load driver chrome
# driver = webdriver.Firefox(firefox_options=options, executable_path='/usr/local/bin/geckodriver')
driver.delete_all_cookies()

# Create empty dataframe
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

# Function for handle error & more flexible
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

# Open each page, putusan3.mahkamahagung.go.id/search.html?q=pilkada has 138 pages
for i in range(1, 138):
    page = 'https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page='
    driver.get(page + str(i))

    # Get url, each pages contain 19-22 pages
    url = []
    for j in range(22):
        items = driver.find_elements_by_xpath(link[j])
        for item in items:
            href = item.get_attribute('href')
            url.append(href)
    print('Page ' + str(i))

    # Open each url
    for k in range(len(url)):
        driver.get(url[k])
        time.sleep(1)

        Xpath = '//*[@id="popular-post-list-sidebar"]/ul/table/tbody/'

        # Get data from each url
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


        # Add new data in new rows
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

    # Export to 'output.xlsx'
    data.to_excel("./output" + str(timenow) + ".xlsx", index=Fasle)

driver.quit()
