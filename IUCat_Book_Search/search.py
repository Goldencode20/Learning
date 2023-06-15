import pandas as pd
import numpy as np
import openpyxl
import requests
import re
from bs4 import BeautifulSoup

\
excel_in = pd.read_excel(r'Projects-Learning\IUCat_Book_Search\Mintz.xlsx')

do_not_have = []
have = []
errors = []

"""
for x in range(len(excel_in.Title)):
    title = excel_in.loc[x].at["Title"]
    title = title.replace(" ", "+") #Set this up to fit the search format
    URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&q=" + title + "&search_field=all_field"
    print(URL)
"""

#for x in range(len(excel_in.Title)):
for x in range(len(excel_in.Title)):
    #print(excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"]) 
    #print(x)
    title = excel_in.loc[x].at["Title"]
    title = title.replace(" ", "+")
    URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&q=" + title + "&search_field=all_field"
    try:
    
        title = re.sub(r"[^a-zA-Z0-9 ]", "", title)
        title = title.lower()

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id = "content")
        search_results = results.find_all("div", class_="document blacklight-book")
        if(len(search_results) == 0):
            do_not_have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Not in system", URL])
        else: 
            not_found_flag = True

            for search_result in search_results:
                search_title = search_result.find("h3", class_="index_title document-title-heading col-sm-9 col-lg-10")
                search_author = search_result.find("dd", class_="blacklight-author_display")

                search_title = search_title.text
                search_title = search_title.replace(" ", "+")
                search_title = re.sub(r"[^a-zA-Z ]", "", search_title)
                search_title = search_title.lower()

                if(search_author == None):
                    search_author = "No Author"
                else:
                    search_author = search_author.text
                search_author = search_author.replace(" ", "+")
                search_author = re.sub(r"[^a-zA-Z ]", "", search_author)
                search_author = search_author.lower()
                author = excel_in.loc[x].at["Author"]
                author = author.replace(" ", "+")
                author = re.sub(r"[^a-zA-Z ]", "", author)
                author = author.lower()

                if(search_title == title and search_author == author and not_found_flag):
                    not_found_flag = False

            if(not_found_flag):
                do_not_have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Fuzzy", URL])
            else:
                have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"]])
    except:
        errors.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Error", URL])

do_not_have = do_not_have + errors
do_not_have_np = np.array(do_not_have)
have_np = np.array(have)
do_not_have_df = pd.DataFrame(do_not_have_np, columns = ['Title', 'Author', 'Reason', 'URL'])
have_df = pd.DataFrame(have_np, columns = ['Title', 'Author'])
with pd.ExcelWriter('return1.xlsx') as writer:
    do_not_have_df.to_excel(writer, sheet_name = "Possible Libraries Do Not Have")
    have_df.to_excel(writer, sheet_name = "Libraries Have")


#TODO UI
#TODO If has x chance to be same book you can say we have.