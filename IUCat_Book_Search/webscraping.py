import requests
from bs4 import BeautifulSoup
"""
URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&q=sugar+a+bittersweet+history&search_field=all_field"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "content")
#print(results.prettify())

search_results = results.find_all("div", class_="document blacklight-book")

#print(search_results)

for search_result in search_results:
    search_title = search_result.find("h3", class_="index_title document-title-heading col-sm-9 col-lg-10")
    search_author = search_result.find("dd", class_="blacklight-author_display")
    print(search_title.text)
    print(search_author.text, "\n")
"""

#print(search_form)
#search_bar = search_form.find("input", class_="form-control q flex-item")
#print(search_bar)

URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&search_field=all_field&q=njkadsf"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id = "content")
#print(results.prettify())
results = soup.find(id = "main-container")
search_results = results.find_all("div", class_="row")
for search_result in search_results:
    print(search_result, end="\n"*2)