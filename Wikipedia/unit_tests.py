import unittest
import time
from bs4 import BeautifulSoup
import requests
import string


class UnitTestsDataMiningWikipedia(unittest.TestCase):
    def test_extract_the_title_of_the_topic(self):
        print("test_extract_the_title_of_the_topic")

        url = 'https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence'

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#firstHeading") is not None:
            print("title : " + str(soup.select_one("#firstHeading").text))

    def test_extract_the_body_content_of_the_topic(self):
        print("test_extract_the_title_of_the_topic")

        url = 'https://en.wikipedia.org/wiki/Outline_of_artificial_intelligence'

        # Request the content of a page from the url
        html = requests.get(url)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#bodyContent") is not None:
            print("content : " + str(soup.select_one("#bodyContent").text))


if __name__ == '__main__':
    unittest.main()
