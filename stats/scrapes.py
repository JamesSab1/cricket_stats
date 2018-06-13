from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrape(url, range_length):
    """Scrape cricinfo stats urls with given number of stats columns"""
    html = urlopen(url)

    bsobj = BeautifulSoup(html.read(), "lxml")
    stats = bsobj.find("tbody").findAll("td")

    stats_list = []
    for td in stats:
        stats_list.append(td.text)
    big_list = []
    for i in range(0, len(stats_list), range_length):
        big_list.append(stats_list[i:i + range_length])
    return big_list
