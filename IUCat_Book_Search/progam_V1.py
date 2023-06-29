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

import tkinter as tk
import pandas as pd
import numpy as np
import openpyxl
import requests
import re
from bs4 import BeautifulSoup
from tkinter import filedialog
from difflib import SequenceMatcher

def program(file, path, label):
    
    #This is where we get the excel file in question and we pull it into the file
    excel_in = pd.read_excel(file) 

    #Set up lists for the output files
    do_not_have = []
    fuzzy = []
    no_Author = []
    have = []
    errors = []

    #Run for each line in the excel sheet
    searchLines = (len(excel_in.Title))
    for x in range(searchLines):
    #for x in range(5):
        #Update the label
        if (x % 10 == 0):
            label.configure(text = str(x) + "/" + str(searchLines))
            label.update()

        #Get author and normalize if one is listed otherwise leave author blank
        author = excel_in.loc[x].at["Author"]
        if(type(author) != float):
            author = author.replace(" ", "+")
        else:
            author = ""

        #Get the title and normalize it
        title = excel_in.loc[x].at["Title"]
        title = title.replace(" ", "+")

        #Make the URL
        URL = "https://iucat.iu.edu/?utf8=%E2%9C%93&q=" + title + "+" + author + "&search_field=all_field"

        #Try this and if something happens mark it as an error
        try:
            
            #Normalize the title and author
            title = excel_in.loc[x].at["Title"]
            title = title.replace(" ", "+")
            title = re.sub(r"[^a-zA-Z0-9 ]", "", title)
            title = title.lower()
            author = re.sub(r"[^a-zA-Z ]", "", author)
            author = author.lower()

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
                #Set up the higest match percent
                highest_score = 0

                #For each possible search result if it matches
                for search_result in search_results:
                    
                    #Get the search result title and author
                    search_title = search_results[0].find("h3", class_="index_title document-title-heading col-sm-9 col-lg-10")
                    search_author = search_result.find("dd", class_="blacklight-author_display")

                    #Normalize the title and to match we have it written
                    search_title = search_title.text
                    search_title = search_title.replace(" ", "+")
                    search_title = re.sub(r"[^a-zA-Z ]", "", search_title)
                    search_title = search_title.lower()

                    #Get author if one is listed otherwise mark "No Author"
                    if(search_author == None):
                        search_author = ""
                    else:
                        search_author = search_author.text

                    #Normalize the author 
                    search_author = search_author.replace(" ", "+")
                    search_author = re.sub(r"[^a-zA-Z ]", "", search_author)
                    search_author = search_author.lower()

                    #Calulate how related the title and author are then take the average
                    title_score = SequenceMatcher(None, title, search_title).ratio()
                    author_score = SequenceMatcher(None, author, search_author).ratio()
                    total_score = (title_score + author_score) / 2

                    #If the new total score is higher than the old highest score than replace the score
                    if(total_score > highest_score):
                        highest_score = total_score

                #Take the highest score and if it above a certian percent score we set then say fuzzy otherwise add to have list
                if(author == ""):
                    no_Author.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "No Author", URL])
                elif(highest_score <= 0.50):
                    do_not_have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Not in system", URL])
                elif(highest_score < 0.90 and highest_score > 0.50):
                    fuzzy.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Fuzzy", URL])
                else:
                    have.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], URL])
        
        #If the try failed add book to errors list
        except:
            errors.append([excel_in.loc[x].at["Title"], excel_in.loc[x].at["Author"], "Error", URL])

    #Combine the do not have list and errors list for easier reading
    do_not_have = fuzzy + errors + no_Author + do_not_have

    #Add the lists to the output file 
    do_not_have_np = np.array(do_not_have)
    have_np = np.array(have)
    do_not_have_df = pd.DataFrame(do_not_have_np, columns = ['Title', 'Author', 'Reason', 'URL'])
    have_df = pd.DataFrame(have_np, columns = ['Title', 'Author', 'URL'])

    #Write to the output file
    #with pd.ExcelWriter('Results.xlsx') as writer:
    path = path + "/Results.xlsx"
    with pd.ExcelWriter(path) as writer:
        do_not_have_df.to_excel(writer, sheet_name = "Possible Libraries Do Not Have")
        have_df.to_excel(writer, sheet_name = "Libraries Have")
    

#Below is for the UI

app = tk.Tk()

btn_next = tk.Button(
    master = app,
    text = "Run",
    width = 25,
    height = 5,
    bg = "white",
    fg = "black"
)

def handle_click(event):
    USER_FILE = filedialog.askopenfilename()
    print(USER_FILE)
    USER_SAVE = filedialog.askdirectory()
    print(USER_SAVE)
    btn_next.destroy()
    lbl_name.configure(text = "Setting Up")
    program(USER_FILE, USER_SAVE, lbl_name)
    print("Done")
    lbl_name.configure(text = "Done")


lbl_name = tk.Label(master = app, text = "IUCAT book search \n\n How to use: \n 1. Create a new excel file \n 2. Put all Titles into the first column \n 3. Put all Authors into the second column \n 4. Save file \n 5. Hit Run \n 6. Select the newly created excel sheet \n 7. Select the location you want the output to be saved \n 8. Wait this process could take awhile depending on how many books you are checking")
lbl_name.pack()
btn_next.pack()
btn_next.bind("<Button-1>", handle_click)
app.mainloop()


#TODO Figure out the error