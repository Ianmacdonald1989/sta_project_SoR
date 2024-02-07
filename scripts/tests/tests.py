from scripts_links import extract_reference_code
from bs4 import BeautifulSoup

import unittest
class TestExtractReferenceCode(unittest.TestCase):
    def test_extract_code_found(self):
        test_html = "<p> GB243 T/ SOR /2 </p>"
        soup = BeautifulSoup(test_html, 'html.parser')
        extracted_code = extract_reference_code(soup)
        self.assertEqual(extracted_code, "GB243 T/ SOR /2")

    def test_extract_code_not_found(self):
        test_html = "<div>No reference code found.</div>"
        soup = BeautifulSoup(test_html, "html.parser")
        extracted_code = extract_reference_code(soup)
        self.assertEqual(extracted_code, "code not found")



class TestExtractLinks(unittest.TestCase):
    def test_extract_links_found(self):
        test_html = "<p>https://spiritofrevolt.info/collection/</p>"
        soup = BeautifulSoup(test_html, 'html.parser')
        expected_links = ['https://spiritofrevolt.info/?page_id=4327&preview=true', 'https://spiritofrevolt.info/960-2/']
        self.assertIn(expected_links[0], expected_links)
        self.assertIn(expected_links[1], expected_links)

    def test_extract_no_links(self):
        test_html = "<p> No links here </p>"
        soup = BeautifulSoup(test_html, "html.parser")
        extracted_links = extract_reference_code(soup)
        self.assertEqual(extracted_links, "No links here")