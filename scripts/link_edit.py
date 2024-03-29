# import openpyxl
# import requests
# from bs4 import BeautifulSoup
# import webbrowser
# import re

# # import links from excel
# wb = openpyxl.load_workbook("catalogue_database_3.xlsx")
# sheet = wb.active
# links = [(cell[0].value, cell[1].value, cell[2].value) for cell in sheet.iter_rows(min_row=3, max_row=4, min_col=1, max_col=3)]
# print(links[1])



# # retrive web links
# for text, middle_value, link in links:  # Iterate over the links from the Excel sheet
#     response = requests.get(link)
#     response.raise_for_status()
#     html_content = response.text
#     webbrowser.open(link)



# # #reggex 
# soup = BeautifulSoup(html_content, 'html.parser')
# archives_widget = soup.find("li", id="archives-2")
# if archives_widget:
#     archives_widget.decompose()

# with open("modified_page.html", "w") as f:
#     f.write(str(soup))

    
# original attempt
# for tag in soup.find_all('h3', class_="widgettitle"):
#     if tag.string:
#         tag.string = re.sub(r'\s+', ',', tag.string)
    
#     #remove archive column
#     if tag.name == 'li' and all(child.name == 'h3' for child in tag.find_all(True)):
#         print(tag.name, tag.attrs)
#         tag.extract()


# cleaned_html = str(soup)


