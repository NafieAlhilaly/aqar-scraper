from os.path import realpath
import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest
from helpers.cleaner import numbers_from_text, clean_time


BASE_URL = "https://sa.aqar.fm/%D9%81%D9%84%D9%84-%D9%84%D9%84%D8%A8%D9%8A%D8%B9/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6/"
NUMBER_OF_PAGES = 5  # number of pages to read form Aqar website

names_lst = []
sizes_lst = []
prices_lst = []
dates_lst = []

page_number = 0

print("script started")
while page_number < NUMBER_OF_PAGES:
    result = requests.get(f"{BASE_URL}{page_number}")

    if result.status_code != 200:
        print(f"could connect to Aqar server, status code : {result.status_code}")
        break

    soup = bs(result.content, "html.parser")

    # extract data from tags
    names = soup.find_all("a", {"class": "listTitle"})
    sizes = soup.find_all("span", {"class": "size"})
    prices = soup.find_all("span", {"class": "price"})
    time_div = soup.find_all("div", {"class", "timeEtc"})

    # extract date from children tags
    str_time = [str(element) for element in time_div]
    soup = bs("".join(str_time), "html.parser")
    time = soup.find_all("div", {"class", "time"})

    for i in range(len(names)):
        names_lst.append(names[i].text)
        sizes_lst.append(sizes[i].text)
        prices_lst.append(prices[i].text)
        dates_lst.append(time[i].text)

    page_number += 1


prices_lst = numbers_from_text(prices_lst)
sizes_lst = numbers_from_text(sizes_lst)
dates_lst = clean_time(dates_lst)

grouped_data = zip_longest(*[names_lst, sizes_lst, prices_lst, dates_lst])
with open("Aqar.csv", "w", encoding="utf-8") as aqar_file:
    wr = csv.writer(aqar_file)
    wr.writerow(["district_name", "property_size", "property_price", "date"])
    wr.writerows(grouped_data)
    print(f"script finished, csv file saved to {realpath(aqar_file.name)}")
