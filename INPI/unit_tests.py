import unittest
import pymysql
from bs4 import BeautifulSoup
import requests


class UnitTestsDataMiningInpiForOnePatent(unittest.TestCase):
    def test_mining_title_from_one_patent(self):
        print("test_mining_title_from_one_patent")

        url_for_one_patent = 'https://bases-brevets.inpi.fr/fr/document/FR3100422.html'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("h1", {"class": "notice-title"}) is not None:
            print("Title : " + soup.find("h1", {"class": "notice-title"}).text.lower())

    def test_mining_description_from_one_patent(self):
        print("test_mining_description_from_one_patent")

        url_for_one_patent = 'https://bases-brevets.inpi.fr/fr/document/FR3100422.html'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"class": "notice-text"}) is not None:
            description = soup\
                .find("div", {"class": "notice-text"})\
                .text\
                .lower()\
                .replace('\t', ' ')\
                .replace('\n', ' ')\
                .replace('  ', ' ')\
                .replace('\r', ' ')

            print("Description : " + description)


class UnitTestsDataMiningInpiFreeEnergyDevices(unittest.TestCase):
    def test_fr_patent(self):
        print('test_fr_patent')

        keywords = [
            "perpétuel",
            "autogénérateur",
            "sans limite",
            "indéfiniment",
            "générateur d'énergie",
            "générateur électrique",
            "auto-générateur",
            "excès d'énergie"
        ]

        for c1 in range(0, 3999999):
            title = ""
            description = ""

            patent_number = "FR" + str(c1)

            url_patent = "https://bases-brevets.inpi.fr/fr/document/" + patent_number + ".html"

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            # Request the content of a page from the url
            html = requests.get(url_patent, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.text, 'html.parser')

            # title
            if soup.find("h1", {"class": "notice-title"}) is not None:
                title += soup\
                    .find("h1", {"class": "notice-title"})\
                    .text\
                    .lower()\
                    .replace('\t', ' ')\
                    .replace('\n', ' ')\
                    .replace('  ', ' ')\
                    .replace('\r', ' ')

                # description
                if soup.find("div", {"class": "notice-text"}) is not None:
                    description += soup \
                        .find("div", {"class": "notice-text"}) \
                        .text \
                        .lower() \
                        .replace('\t', ' ') \
                        .replace('\n', ' ') \
                        .replace('  ', ' ') \
                        .replace('\r', ' ')

                for keyword in keywords:
                    if keyword in title or keyword in description:
                        x = {
                            'title': title,
                            'patent_number': patent_number,
                            'url_patent': url_patent
                        }

                        try:
                            # Connect to the database
                            connection = pymysql.connect(
                                host='localhost',
                                port=3306,
                                user='',
                                password='',
                                db='patents',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor
                            )

                            with connection.cursor() as cursor:
                                try:
                                    sql = "INSERT INTO `free_energy_inventions` (" \
                                          "`title`, " \
                                          "`patent_number`, " \
                                          "`url_patent`) VALUE (%s, %s, %s)"

                                    cursor.execute(sql, (
                                        x.get('title'),
                                        x.get('patent_number'),
                                        x.get('url_patent')
                                    ))

                                    connection.commit()

                                    print('Patent ' + x.get('patent_number') + ' : ok')

                                    connection.close()
                                except Exception as e:
                                    print("The record already exists (patent " + x.get('patent_number') + ") : " + str(e))
                                    connection.close()
                        except Exception as e:
                            print("Problem connection MySQL : " + str(e))

                        break
                    else:
                        print('no keyword "' + keyword + '" in patent ' + patent_number)
            else:
                print("patent " + patent_number + " : no information")


if __name__ == '__main__':
    unittest.main()
