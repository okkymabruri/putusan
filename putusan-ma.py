"""
author: Okky Mabruri
maintainer: Okky Mabruri <okkymbrur@gmail.com>
"""

import argparse
import io
import os
import re
import time
import urllib
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import date

import pandas as pd
import requests
import utils
from bs4 import BeautifulSoup
from pdfminer import high_level


def get_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Putusan Mahkamah Agung Scraper", add_help=True
    )
    parser.add_argument(
        "-k",
        "--keyword",
        required=False,
        dest="keyword",
        help="keyword for the Supreme Court",
    )
    parser.add_argument(
        "-u",
        "--url",
        required=False,
        dest="url",
        help=" specify url for the Supreme Court\nexample: https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56",
    )
    parser.add_argument(
        "-sd",
        "--sortdate",
        dest="sort_date",
        required=False,
        default=False,
        action="store_true",
        help="(optional) scraping from newest putusan. Default False",
    )
    parser.add_argument(
        "-dp",
        "--downloadpdf",
        dest="download_pdf",
        required=False,
        default=False,
        action="store_true",
        help="(optional) download pdf. Default False",
    )
    return parser.parse_args(argv)


def open_page(link):
    count = 0
    while count < 3:
        try:
            return BeautifulSoup(requests.get(link).text, "lxml")
        except:
            count += 1
            time.sleep(5)


def get_detail(soup, keyword):
    try:
        text = (
            soup.find(lambda tag: tag.name == "td" and keyword in tag.text)
            .find_next()
            .get_text()
            .strip()
        )
        return text
    except:
        return ""


def get_pdf(url, path_pdf, download_pdf):
    file = urllib.request.urlopen(url)
    file_name = file.info().get_filename().replace("/", " ")
    # with file:
        # file = file.read()
    file = file.read()
    if download_pdf:
        with open(f"{path_pdf}/{file_name}", "wb") as out_file:
            out_file.write(file)

    return io.BytesIO(file), file_name


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


def extract_data(link, keyword_url):
    global today
    global path_output
    global path_pdf
    global download_pdf

    soup = open_page(link)
    table = soup.find("table", {"class": "table"})
    judul = table.find("h2").text
    soup.find("table", {"class": "table"}).find("h2").decompose()

    nomor = get_detail(table, "Nomor")
    tingkat_proses = get_detail(table, "Tingkat Proses")
    klasifikasi = get_detail(table, "Klasifikasi")
    kata_kunci = get_detail(table, "Kata Kunci")
    tahun = get_detail(table, "Tahun")
    tanggal_register = get_detail(table, "Tanggal Register")
    lembaga_peradilan = get_detail(table, "Lembaga Peradilan")
    jenis_lembaga_peradilan = get_detail(table, "Jenis Lembaga Peradilan")
    hakim_ketua = get_detail(table, "Hakim Ketua")
    hakim_anggota = get_detail(table, "Hakim Anggota")
    panitera = get_detail(table, "Panitera")
    amar = get_detail(table, "Amar")
    amar_lainnya = get_detail(table, "Amar Lainnya")
    catatan_amar = get_detail(table, "Catatan Amar")
    tanggal_musyawarah = get_detail(table, "Tanggal Musyawarah")
    tanggal_dibacakan = get_detail(table, "Tanggal Dibacakan")
    kaidah = get_detail(table, "Kaidah")
    abstrak = get_detail(table, "Abstrak")

    try:
        link_pdf = soup.find("a", href=re.compile(r"/pdf/"))["href"]
        file_pdf, file_name_pdf = get_pdf(link_pdf, path_pdf, download_pdf)
        text_pdf = high_level.extract_text(file_pdf)
        text_pdf = clean_text(text_pdf)
    except:
        link_pdf = ""
        text_pdf = ""
        file_name_pdf = ""

    data = [
        judul,
        nomor,
        tingkat_proses,
        klasifikasi,
        kata_kunci,
        tahun,
        tanggal_register,
        lembaga_peradilan,
        jenis_lembaga_peradilan,
        hakim_ketua,
        hakim_anggota,
        panitera,
        amar,
        amar_lainnya,
        catatan_amar,
        tanggal_musyawarah,
        tanggal_dibacakan,
        kaidah,
        abstrak,
        link,
        link_pdf,
        file_name_pdf,
        text_pdf,
    ]
    result = pd.DataFrame(
        [data],
        columns=[
            "judul",
            "nomor",
            "tingkat_proses",
            "klasifikasi",
            "kata_kunci",
            "tahun",
            "tanggal_register",
            "lembaga_peradilan",
            "jenis_lembaga_peradilan",
            "hakim_ketua",
            "hakim_anggota",
            "panitera",
            "amar",
            "amar_lainnya",
            "catatan_amar",
            "tanggal_musyawarah",
            "tanggal_dibacakan",
            "kaidah",
            "abstrak",
            "link",
            "link_pdf",
            "file_name_pdf",
            "text_pdf",
        ],
    )

    keyword_url = keyword_url.replace("/", " ")
    if keyword_url.startswith("https"):
        keyword_url = ""

    destination = f"{path_output}/putusan_ma_{keyword_url}_{today}"
    print(destination)
    if not os.path.isfile(f"{destination}.csv"):
        result.to_csv(f"{destination}.csv", header=True, index=False)
    else:
        result.to_csv(f"{destination}.csv", mode="a", header=False, index=False)


def run_process(keyword_url, page, sort_page):

    if keyword_url.startswith("https"):
        link = f"{keyword_url}&page={page}"
    else:
        link = f"https://putusan3.mahkamahagung.go.id/search.html?q={keyword_url}&page={page}"
    if sort_page:
        link = f"{link}&obf=TANGGAL_PUTUS&obm=desc"

    print(link)

    soup = open_page(link)
    links = soup.find_all("a", {"href": re.compile("/direktori/putusan")})

    for link in links:
        extract_data(link["href"], keyword_url)


if __name__ == "__main__":
    args = get_args()
    keyword = args.keyword
    url = args.url
    sort_date = args.sort_date
    download_pdf = args.download_pdf

    if not keyword and not url:
        exit("Please provide keyword or URL")

    # keyword = "Pdt.Sus-BPSK"
    path_output = utils.create_path("putusan")
    path_pdf = utils.create_path("pdf-putusan")

    today = date.today().strftime("%Y-%m-%d")

    link = f"https://putusan3.mahkamahagung.go.id/search.html?q={keyword}&page=1"

    if url:
        link = url

    soup = open_page(link)

    last_page = int(
        soup.find_all("a", {"class": "page-link"})[-1].get("data-ci-pagination-page")
    )

    if url:
        print(f"Scraping with url: {url} - {20 * last_page} data - {last_page} page")
    else:
        print(
            f"Scraping with keyword: {keyword} - {20 * last_page} data - {last_page} page"
        )

    # url = "https://putusan3.mahkamahagung.go.id/search.html?q=&jenis_doc=&cat=98821d8a4bc63aff3a81f66c37934f56"
    # url = "https://putusan3.mahkamahagung.go.id/search.html?cat=98821d8a4bc63aff3a81f66c37934f56&page=2"

    if url:
        keyword_url = url
    else:
        keyword_url = keyword

    futures = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        for page in range(last_page):
            futures.append(
                executor.submit(run_process, keyword_url, page + 1, sort_date)
            )
    wait(futures)
