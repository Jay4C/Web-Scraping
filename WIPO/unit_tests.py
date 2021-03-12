import unittest
import pymysql
from bs4 import BeautifulSoup
import requests


class UnitTestsDataMiningWipoForOnePatent(unittest.TestCase):
    def test_mining_title_from_one_patent(self):
        print("test_mining_title_from_one_patent")

        url_for_one_patent = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020188266'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"class": "ps-page-header--subtitle--text"}) is not None:
            title = soup\
                .find("div", {"class": "ps-page-header--subtitle--text"})\
                .text\
                .lower()\
                .replace('\t', ' ')\
                .replace('\n', ' ')\
                .replace('  ', ' ')\
                .replace('\r', ' ')

            print("Title : " + title)

    def test_mining_abstract_from_one_patent(self):
        print("test_mining_abstract_from_one_patent")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_for_one_patent = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020188266&tab=PCTBIBLIO'
        html = requests.get(url_for_one_patent, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"class": "patent-abstract"}) is not None:
            abstract = soup\
                .find("div", {"class": "patent-abstract"})\
                .text\
                .lower()\
                .replace('\t', ' ')\
                .replace('\n', ' ')\
                .replace('  ', ' ')\
                .replace('\r', ' ')

            print("Abstract : " + abstract)

    def test_mining_description_from_one_patent(self):
        print("test_mining_description_from_one_patent")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_for_one_patent = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020188266&tab=PCTDESCRIPTION'
        html = requests.get(url_for_one_patent, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"class": "ps-panel--content font-size--small"}) is not None:
            description = soup\
                .find("div", {"class": "ps-panel--content font-size--small"})\
                .text\
                .lower()\
                .replace('\t', ' ')\
                .replace('\n', ' ')\
                .replace('  ', ' ')\
                .replace('\r', ' ')

            print("Description : " + description)

    def test_mining_claims_from_one_patent(self):
        print("test_mining_claims_from_one_patent")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_for_one_patent = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020188266&tab=PCTCLAIMS'
        html = requests.get(url_for_one_patent, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"class": "ps-panel--content font-size--small"}) is not None:
            claims = soup\
                .find("div", {"class": "ps-panel--content font-size--small"})\
                .text\
                .lower()\
                .replace('\t', ' ')\
                .replace('\n', ' ')\
                .replace('  ', ' ')\
                .replace('\r', ' ')

            print("claims : " + claims)


class UnitTestsDataMiningWipoFreeEnergyDevices(unittest.TestCase):
    def test_wo_patent(self):
        print('test_wo_patent')

        keywords = [
            "anti-gravity",
            "transmutation",
            "mutation",
            "zero point energy",
            "free energy",
            "perpetual",
            "self-running",
            "self-powered",
            "self running",
            "self powered",
            "self-maintained",
            "self maintained",
            "self-run",
            "self run",
            "self-generator",
            "self generator",
            "earth battery",
            "earth-battery",
            "ground battery",
            "earth generator",
            "ground generator",
            "overunity",
            "perpetual motion",
            "indefinitely",
            "unlimited",
            "without limit",
            "electrical generator",
            "electrical battery",
            "magnet"
        ]

        for c1 in range(25, 99999999):
            title = ""
            abstract = ""
            description = ""
            claims = ""

            patent_number = "WO" + str(c1)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            url_title = "https://patentscope.wipo.int/search/en/detail.jsf?docId=" + patent_number + "&tab=PCTBIBLIO"
            html_title = requests.get(url_title, headers=headers)
            soup_title = BeautifulSoup(html_title.text, 'html.parser')

            # title
            if soup_title.find("div", {"class": "ps-page-header--subtitle--text"}) is not None:
                title += soup_title \
                    .find("div", {"class": "ps-page-header--subtitle--text"}) \
                    .text \
                    .lower() \
                    .replace('\t', ' ') \
                    .replace('\n', ' ') \
                    .replace('  ', ' ') \
                    .replace('\r', ' ')

                url_abstract = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=' + patent_number + '&tab=PCTBIBLIO'
                html_abstract = requests.get(url_abstract, headers=headers)
                soup_abstract = BeautifulSoup(html_abstract.text, 'html.parser')

                if soup_abstract.find("div", {"class": "patent-abstract"}) is not None:
                    abstract += soup_abstract \
                        .find("div", {"class": "patent-abstract"}) \
                        .text \
                        .lower() \
                        .replace('\t', ' ') \
                        .replace('\n', ' ') \
                        .replace('  ', ' ') \
                        .replace('\r', ' ')

                url_for_description = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=' + patent_number + '&tab=PCTDESCRIPTION'
                html_description = requests.get(url_for_description, headers=headers)
                soup_description = BeautifulSoup(html_description.text, 'html.parser')

                if soup_description.find("div", {"class": "ps-panel--content font-size--small"}) is not None:
                    description += soup_description \
                        .find("div", {"class": "ps-panel--content font-size--small"}) \
                        .text \
                        .lower() \
                        .replace('\t', ' ') \
                        .replace('\n', ' ') \
                        .replace('  ', ' ') \
                        .replace('\r', ' ')

                url_for_claims = 'https://patentscope.wipo.int/search/en/detail.jsf?docId=' + patent_number + '&tab=PCTCLAIMS'
                html_claims = requests.get(url_for_claims, headers=headers)
                soup_claims = BeautifulSoup(html_claims.text, 'html.parser')

                if soup_claims.find("div", {"class": "ps-panel--content font-size--small"}) is not None:
                    claims += soup_claims \
                        .find("div", {"class": "ps-panel--content font-size--small"}) \
                        .text \
                        .lower() \
                        .replace('\t', ' ') \
                        .replace('\n', ' ') \
                        .replace('  ', ' ') \
                        .replace('\r', ' ')

                for keyword in keywords:
                    if keyword in title or keyword in abstract or keyword in description or keyword in claims:
                        x = {
                            'title': title,
                            'patent_number': patent_number,
                            'url_patent': 'https://patentscope.wipo.int/search/en/detail.jsf?docId' + patent_number
                        }

                        try:
                            # Connect to the database
                            connection = pymysql.connect(
                                host='localhost',
                                port=3306,
                                user='root',
                                password='v2HJJzexYxlp0D0So77ztwMOKEKu97@@@@@@',
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
                                    print(
                                        "The record already exists (patent " + x.get(
                                            'patent_number') + ") : " + str(e))
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
