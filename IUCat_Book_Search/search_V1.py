"""
Author: 
Creed Jones

Summary: 
Program to take in an excel sheet of books then
search IUCAT if the books are in the system and
mark if they are. Used to save time so that librians
don't need search hurndeds of books that are being 
donated from other libraries. 
"""

import pandas as pd
import numpy as np
import openpyxl
import requests
import re
from bs4 import BeautifulSoup

#This is where we get the excel file in question and we pull it into the file
#TODO Get file from user
excel_in = pd.read_excel(r'Projects-Learning\IUCat_Book_Search\Mintz.xlsx') 

#Set up lists for the output files
do_not_have = []
have = []
errors = []

#Run for each line in the excel sheet
for x in range(len(excel_in.Title)):

    #Make the URL
    #TODO Set up the search for Author not title (Might yeild better results)
    #TODO If not author run this code (Ask if that is requested outcome from Iliana)
    title = excel_in.loc[x].at["Title"]
    title = title.replace(" ", "+")
    URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&q=" + title + "&search_field=all_field"

    #Try this and if something happens mark it as an error
    try:
        
        #Normalize the title
        title = re.sub(r"[^a-zA-Z0-9 ]", "", title)
        title = title.lower()

        #Search the HTML for the title
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id = "content")
        search_results = results.find_all("div", class_="document blacklight-book")

        #Check if there are any search results
        if(len(search_results) == 0):
            #If none mark not in system
            do_not_have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Not in system", URL])
        else: 
            #Set up that we have not found the entry
            not_found_flag = True

            #For each possible search result if it matches
            for search_result in search_results:
                
                #Get the search result title and author
                search_title = search_result.find("h3", class_="index_title document-title-heading col-sm-9 col-lg-10")
                search_author = search_result.find("dd", class_="blacklight-author_display")

                #Normalize the title and to match we have it written
                search_title = search_title.text
                search_title = search_title.replace(" ", "+")
                search_title = re.sub(r"[^a-zA-Z ]", "", search_title)
                search_title = search_title.lower()

                #Get author if one is listed otherwise mark "No Author"
                if(search_author == None):
                    search_author = "No Author"
                else:
                    search_author = search_author.text

                #Normalize the author 
                search_author = search_author.replace(" ", "+")
                search_author = re.sub(r"[^a-zA-Z ]", "", search_author)
                search_author = search_author.lower()
                author = excel_in.loc[x].at["Author"]
                author = author.replace(" ", "+")
                author = re.sub(r"[^a-zA-Z ]", "", author)
                author = author.lower()

                #Check if the titles match, the authors match, and if we have already found the book 
                #TODO Work out some fuzziness and want x amount of accuracy
                if(search_title == title and search_author == author and not_found_flag):
                    not_found_flag = False

            #If the book is not found add to do not have list otherwise add to found list
            if(not_found_flag):
                do_not_have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Fuzzy", URL])
            else:
                have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"]])
    
    #If the try failed add book to errors list
    except:
        errors.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Error", URL])

#Combine the do not have list and errors list for easier reading
do_not_have = do_not_have + errors

#Add the lists to the output file 
do_not_have_np = np.array(do_not_have)
have_np = np.array(have)
do_not_have_df = pd.DataFrame(do_not_have_np, columns = ['Title', 'Author', 'Reason', 'URL'])
have_df = pd.DataFrame(have_np, columns = ['Title', 'Author'])

#Write to the output file
#TODO Let user pick output file name
with pd.ExcelWriter('Book_Search.xlsx') as writer:
    do_not_have_df.to_excel(writer, sheet_name = "Possible Libraries Do Not Have")
    have_df.to_excel(writer, sheet_name = "Libraries Have")


#TODO UI