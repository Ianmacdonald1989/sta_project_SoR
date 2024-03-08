import openpyxl
import requests
from bs4 import BeautifulSoup

# URL of the HTML page
url = 'https://spiritofrevolt.info/collection/'

# Get HTML content
response = requests.get(url)
html_content = response.content

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Create an Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Extract data
catalogue_rows = []
for catalogue_link in soup.find_all('strong'):
    link = catalogue_link.find('a')
    if link:
        text = link.text.strip()
        url = link['href']
        catalogue_rows.append([text, url])
    else:
        catalogue_rows.append([catalogue_link.text.strip(), ''])

# Write data to Excel
for row in catalogue_rows:
    sheet.append(row)

# Save the Excel file
workbook.save("catalogue_database.xlsx")
print({catalogue_link[0]: catalogue_link[1] for catalogue_link in catalogue_rows})

