import requests
from bs4 import BeautifulSoup


def monster_Search(url):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    """
    links=soup.find_all("a")
    for link in links:
        print(link.get("href"))
    """
    g_data = soup.find_all("div", {"class": "js_result_details-left"})
    for item in g_data:
        print(item.find_all("span")[0].text)
        try:
            print(item.find_all("span")[1].text)
        except:
            pass
        try:
            print(item.find_all("a")[2].text.strip())
        except:
            pass
        print()


monster_Search("https://www.monster.com/jobs/search/?where=New-York&page=6")
a = input("Value? => ")
print(a)
