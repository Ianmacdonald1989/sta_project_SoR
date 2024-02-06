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

# Extract reference data
catalogue_rows = []
for catalogue_reference in soup.find_all('strong'):
    ref = catalogue_reference.find('p')
    if ref:
        text = ref.text.strip()
        ref = ref['span']
        catalogue_rows.append([text, ref])
    else:
        catalogue_rows.append([catalogue_reference.text.strip(), ''])

# Write data to Excel
for row in catalogue_rows:
    sheet.append(row)

# Save the Excel file
workbook.save("catalogue_database_2.xlsx")
print({catalogue_reference[0]: catalogue_reference[1] for catalogue_reference in catalogue_rows})

