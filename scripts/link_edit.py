import openpyxl
import requests
from bs4 import BeautifulSoup
import webbrowser
import re

# import links from excel
wb = openpyxl.load_workbook("catalogue_database_3.xlsx")
sheet = wb.active
links = [(cell[0].value, cell[1].value) for cell in sheet.iter_rows(min_row=2, max_row=3, min_col=1, max_col=2)]
print(links[1])



# edit links
for text, link in links:  # Iterate over the links from the Excel sheet
    reponse = requests.get(link)
    response.raise_for_status()
    html_content = response.text
    webbrowser.open(link)


#   Fetch and clean the HTML
#   cleaned_data = fetch_and_parse(link)  # Call your function

#   if cleaned_data:
#     # logic for processing 
#     print(f"Cleaned data from {link}: {cleaned_data}")