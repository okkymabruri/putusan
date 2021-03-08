#################################################################################
# author: Okky Mabruri
# email: okkymabrur@gmail.com
# usage: python putusan-ma.py -p https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56 -o putusanUUITE
#################################################################################

import argparse

# Importing packages
import datetime  # module datetime for dealing with dates and times
import re  # regex
import time  # time library to manipulate time (pause, etc)

import pandas as pd  # pandas library fpr data processing
from bs4 import BeautifulSoup
from selenium import webdriver  # webdriver from selenium framework to load web
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

parser = argparse.ArgumentParser(
    description="Putusan Mahkamah Agung Scraper", add_help=True
)
parser.add_argument(
    "-p",
    "--page",
    required=True,
    dest="page",
    help="Masukkan link pencarian putusan pilkada",
)
parser.add_argument(
    "-o",
    "--output",
    required=False,
    dest="file_name",
    default="output",
    help="masukkan nama output file, misal UUITE",
)

parser.add_argument(
    "-he",
    "--headless",
    required=False,
    dest="headless",
    default=False,
    help="masukkan nama output file, misal UUITE",
)

args = parser.parse_args()
page = args.page
file_name = args.file_name
headless = args.headless

def runbrowser(headless):
    options = webdriver.ChromeOptions()
    options.headless = headless
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


# get last page
def get_last_page():
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    last_page = soup.find_all("a", attrs={"class": "page-link"})[-1][
        "data-ci-pagination-page"
    ]
    return last_page


def get_link():
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    links = [
        a.get("href")
        for a in soup.find_all(
            "a",
            attrs={
                "href": re.compile(
                    "https://putusan3.mahkamahagung.go.id/direktori/putusan/"
                )
            },
        )
    ]
    return links


def get_data(link):
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    jumlahview = soup.find("div", attrs={"title": "Jumlah view"}).get_text()
    jumlahdl = soup.find("div", attrs={"title": "Jumlah download"}).get_text()
    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    df = df.T
    df.columns = df.iloc[0]
    df = df.rename(columns={df.columns[0]: "Judul"})
    df = df[1:]
    df["Jumlah View"] = jumlahview
    df["Jumlah Download"] = jumlahdl
    df["Link"] = link
    return df


driver = runbrowser(headless)
# page = "https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56"
page = page + "&obf=TANGGAL_PUTUS&obm=desc"  # sort by tanggal putusan
driver.get(page)

timenow = datetime.datetime.now().strftime("%m-%d-%Y")
last_page = get_last_page()

result = pd.DataFrame(None)
for i in range(1, int(last_page)+1):
    print("=========== Scraping Page " + str(i) + "===========")
    driver.get(page + "&page=" + str(i))
    links = get_link()
    for link in links:
        df = get_data(link)
        result = result.append(df)
    print("Total data: " + str(result.shape[0]))

# Export to '.csv'
result.to_csv(file_name + str(timenow) + ".csv", index=False)
driver.quit()