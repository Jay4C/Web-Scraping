import time
import unittest
import requests
from bs4 import BeautifulSoup


class UnitTestsDataMiningIndeed(unittest.TestCase):
    def test_extract_all_ad_link_from_one_page(self):
        print('test_extract_all_ad_link_from_one_page')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://fr.indeed.com/jobs?q=freelance+informatique&l=France&start=0"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"data-tn-element": "jobTitle"}) is not None:
            all_a = soup.find_all("a", {"data-tn-element": "jobTitle"})

            for a in all_a:
                link = "https://fr.indeed.com" + a.get('href')
                print("link of the ad : " + link)
        else:
            print("no ads")

    def test_extract_all_ad_link_from_all_pages(self):
        print('test_extract_all_ad_link_from_all_pages')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        for i in range(0, 77):
            print('page : ' + str(i))

            start = str(10*i)

            url = "https://fr.indeed.com/jobs?q=freelance+informatique&l=France&start=" + start

            time.sleep(10)

            # Request the content of a page from the url
            html = requests.get(url, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("a", {"data-tn-element": "jobTitle"}) is not None:
                all_a = soup.find_all("a", {"data-tn-element": "jobTitle"})

                for a in all_a:
                    link = "https://fr.indeed.com" + a.get('href')
                    print("link of the ad : " + link)
            else:
                print("no ads")

    def test_print_ten_multiplication(self):
        print('test_print_ten_multiplication')

        for i in range(0, 78):
            print(str(10*i))


if __name__ == '__main__':
    unittest.main()
