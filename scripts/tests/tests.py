import unittest
from bs4 import BeautifulSoup
import requests
from unittest.mock import patch, MagicMock  

def extract_reference_code(linked_page_soup):
  ref_code_element = linked_page_soup.find("p")
  if ref_code_element:
    return ref_code_element.text.strip()
  else:
    return "code not found"

class TestExtractReferenceCode(unittest.TestCase):
  def test_extract_code_found(self):
    # Test HTML with code in a paragraph
    test_html = "<p> GB243 T/ SOR /2 </p>"
    soup = BeautifulSoup(test_html, 'html.parser')
    extracted_code = extract_reference_code(soup)
    self.assertEqual(extracted_code, "GB243 T/ SOR /2")

  def test_extract_code_not_found(self):
    # Test HTML with no paragraph
    test_html = "<div>This is some text</div>"
    soup = BeautifulSoup(test_html, 'html.parser')
    extracted_code = extract_reference_code(soup)
    self.assertEqual(extracted_code, "code not found")


def extract_link_data(url):
  # Get HTML content 
  response = requests.get(url)
  html_content = response.content

  # Parse HTML using BeautifulSoup
  soup = BeautifulSoup(html_content, 'html.parser')

  # Extract link data
  catalogue_rows = []
  for catalogue_link in soup.find_all('p'):
    link = catalogue_link.find('a')
    if link:
      text = link.text.strip()
      url = link['href']
      catalogue_rows.append({'text': text, 'url': url})

  return catalogue_rows

class TestExtractLinkData(unittest.TestCase):
  @patch('requests.get') 
  def test_extract_link_data(self, mock_get):
    mock_response = MagicMock()
    mock_response.content = '<p><a href="https://spiritofrevolt.info/collection/">Text</a></p>'  
 
    mock_get.return_value = mock_response

    # Extract link data
    extracted_links = extract_link_data('https://spiritofrevolt.info/collection/')

    # Assert expected results
    self.assertEqual(extracted_links, [
        {'text': 'Text', 'url': 'https://spiritofrevolt.info/collection/'},
        
    ])

if __name__ == '__main__':
  unittest.main()




