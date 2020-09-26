#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[8]:


#Importing packages
from selenium import webdriver
import pandas as pd


# In[ ]:


https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page=1

https://putusan3.mahkamahagung.go.id/search.html?q=pilkada&page=137



html(/body/div[1]/section/div/div/section/div/div[2]/div[3]/div/strong/a)

html(/body/div[1]/section/div/div/section/div/div[2]/div[5]/div/strong/a)
html(/body/div[1]/section/div/div/section/div/div[2]/div[22]/div/strong/a)





html(/body/div[1]/section/div/div/section/div/div[2]/div[22]/div/strong/a)


# In[31]:


driver = webdriver.Chrome('/usr/local/bin/chromedriver')


# In[32]:


driver.get('https://putusan3.mahkamahagung.go.id/direktori/putusan/06c05c2759b6926fab71e70047d407a1.html')


# In[53]:


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


# In[ ]:


Xpath = /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/
#tr[12]/td[2]

Nomor =  driver.find_elements_by_xpath(Xpath, tr[1]/td[2]'

ParaPihak tr[2]/td[2]

TingkatProses tr[3]/td[2]

Klasifikasi tr[4]/td[2]

Tahun tr[5]/td[2]

TanggalRegister tr[6]/td[2]

LembagaPeradilan tr[7]/td[2]/a

JenisLembagaPeradilan tr[8]/td[2]

HakimKetua tr[9]/td[2]

HakimAnggota tr[10]/td[2]

Panitera tr[11]/td[2]

Amar tr[12]/td[2]

CatatanAmar tr[13]/td[2]

TanggalMusyawarah tr[14]/td[2]

TanggalDibacakan tr[15]/td[2]

Kaidah tr[16]/td[2]

Status tr[17]/td[2]


# Nomor /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[1]/td[2]
# 
# ParaPihak /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[2]/td[2]
# 
# TingkatProses /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[3]/td[2]
# 
# Klasifikasi /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[4]/td[2]
# 
# Tahun /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[5]/td[2]
# 
# TanggalRegister /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[6]/td[2]
# 
# LembagaPeradilan /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[7]/td[2]/a
# 
# JenisLembagaPeradilan /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[8]/td[2]
# 
# HakimKetua /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[9]/td[2]
# 
# HakimAnggota /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[10]/td[2]
# 
# Panitera /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[11]/td[2]
# 
# Amar /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[12]/td[2]
# 
# CatatanAmar /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[13]/td[2]
# 
# TanggalMusyawarah /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[14]/td[2]
# 
# TanggalDibacakan /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[15]/td[2]
# 
# Kaidah /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[16]/td[2]
# 
# Status /html/body/div[1]/section[2]/div/div/section/div/div/div[1]/div/div/div/div[1]/div/ul/table/tbody/tr[17]/td[2]
