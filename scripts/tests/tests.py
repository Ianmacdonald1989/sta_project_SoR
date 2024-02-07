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