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
import io
import urllib.request
import ssl
from pdfminer import high_level


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
    dest="headless",
    required=False,
    default=False,
    action="store_true",
    help="(optional) headless",
)

parser.add_argument(
    "-sp",
    "--startpage",
    required=False,
    dest="startpage",
    default="1",
    help="masukkan start page",
)

parser.add_argument(
    "-ep",
    "--endpage",
    required=False,
    dest="last_page",
    default=None,
    help="masukkan end page",
)

args = parser.parse_args()
page = args.page
file_name = args.file_name
headless = args.headless
startpage = args.startpage
last_page = args.last_page

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

def get_pdf(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    open = urllib.request.urlopen(url, context=ctx).read()
    return io.BytesIO(open)

def clean_text(text):
    text = text.replace("M a h ka m a h A g u n g R e p u blik In d o n esia\n", "")
    text = text.replace("Disclaimer\n", "")
    text = text.replace(
        "Kepaniteraan Mahkamah Agung Republik Indonesia berusaha untuk selalu mencantumkan informasi paling kini dan akurat sebagai bentuk komitmen Mahkamah Agung untuk pelayanan publik, transparansi dan akuntabilitas\n",
        "",
    )
    text = text.replace(
        "pelaksanaan fungsi peradilan. Namun dalam hal-hal tertentu masih dimungkinkan terjadi permasalahan teknis terkait dengan akurasi dan keterkinian informasi yang kami sajikan, hal mana akan terus kami perbaiki dari waktu kewaktu.\n",
        "",
    )
    text = text.replace(
        "Dalam hal Anda menemukan inakurasi informasi yang termuat pada situs ini atau informasi yang seharusnya ada, namun belum tersedia, maka harap segera hubungi Kepaniteraan Mahkamah Agung RI melalui :\n",
        "",
    )
    text = text.replace(
        "Email : kepaniteraan@mahkamahagung.go.id    Telp : 021-384 3348 (ext.318)\n",
        "",
    )
    return text


def get_data(link):
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    

    table = soup.find("table")
    df = pd.read_html(str(table))[0]
    df = df.iloc[:, :2]
    df = df.dropna()
    df = df.T
    df.columns = df.iloc[0]
    df = df.rename(columns={df.columns[0]: "Judul"})
    df = df[1:]
    
    try:
        jumlahview = soup.find("div", attrs={"title": "Jumlah view"}).get_text()
        jumlahdl = soup.find("div", attrs={"title": "Jumlah download"}).get_text()
        df["Jumlah View"] = jumlahview
        df["Jumlah Download"] = jumlahdl
    except:
        pass
    try:
        link_pdf = soup.find("a", href=re.compile(r"/pdf/"))["href"]
        text_pdf = high_level.extract_text(get_pdf(link_pdf))
        text_pdf = clean_text(text_pdf)
        df["Linkpdf"] = link_pdf
        df["Textpdf"] = text_pdf
    except:
        pass
    
    df["Link"] = link
    df = df[df.columns.drop(list(df.columns[df.columns.str.len() < 4]))]
    
    return df


driver = runbrowser(headless)
# page = "https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56"
page = page + "&obf=TANGGAL_PUTUS&obm=desc"  # sort by tanggal putusan
driver.get(page)

if last_page == None:
    last_page = get_last_page()

print("Start scraping " + page)
print("From page " + startpage + " to page " + last_page)
    
result = pd.DataFrame(None)
for i in range(int(startpage), int(last_page) + 1):
    timenow = datetime.datetime.now().strftime("%m-%d-%Y %H %M")
    
    print("=========== Scraping Page " + str(i) + " ===========")
    driver.get(page + "&page=" + str(i))
    links = get_link()
    for link in links:
        df = get_data(link)
        try:
            result = result.append(df)
        except:
            pass
    print("Total data: " + str(result.shape[0]), ", Kolom: ", str(result.shape[1]))
    
    # Backup tmp
    if i % 25 == 0:
        result.dropna(axis=1, thresh=len(result)*3/4).to_csv(str(file_name) + str(timenow) + ".csv", index=False)

# dropna column with treshold 75% value NA
result = result.dropna(axis=1, thresh=len(result)*3/4)

# Export to '.csv'
result.to_csv(str(file_name) + str(timenow) + ".csv", index=False)
driver.quit()
