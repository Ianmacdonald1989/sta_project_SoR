import openpyxl
import requests
from bs4 import BeautifulSoup
import webbrowser


# Reference code data
def extract_reference_code(linked_page_soup):
  ref_code_element = linked_page_soup.find("p")
  if ref_code_element:
    return ref_code_element.text.strip()
  else:
    return "code not found"


# description data
def extract_description(linked_page_soup):
  description_element = linked_page_soup.find("h2")

  if description_element:
    return description_element.text.strip()
  else:
    return "description not found"

#extract date 
def extract_date(linked_page_soup):
  date_element = linked_page_soup.find_all("p", string=lambda text: "date" in text)
  if date_element:
    return date_element[0].text.strip()
  else:
    return "date not found"




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

# Extract link data
catalogue_rows = []
for catalogue_link in soup.find_all('p'):
  link = catalogue_link.find('a')
  if link:
    text = link.text.strip()
    url = link['href']

    # getting the reference code from individual links
    try:
      response = requests.get(url)  # fetch linked page
      linked_page_soup = BeautifulSoup(response.content, 'html.parser')
      reference_code = extract_reference_code(linked_page_soup)
      description = extract_description(linked_page_soup)
      date_element = extract_date(linked_page_soup)
      catalogue_rows.append([text, url, reference_code, description, date_element])

    except Exception as e:
      print(f"Error processing link {url}: {e}")
      catalogue_rows.append([text, url, reference_code, description, '', ''])  # will handle any errors
  else:
    catalogue_rows.append([catalogue_link.text.strip(), '', ''])

# Write data to Excel
for row in catalogue_rows:
  sheet.append(row)
#
# # Save the Excel file
workbook.save("catalogue_database_3.xlsx")

for catalogue_link in catalogue_rows:
  print(catalogue_link[0], catalogue_link[1])  # text and url
  print(catalogue_link[2])  # reference code
  if len(catalogue_link) > 3:
    print(catalogue_link[3])  # description
  if len(catalogue_link) > 4 and catalogue_link[4]:  # Check if date exists
    print(catalogue_link[4])
  else:
    if catalogue_link[-1] == '':
      print(f"Error processing link {catalogue_link[1]}")
    else:
      print(f"No date found for link {catalogue_link[1]}")
