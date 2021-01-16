import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time


class UnitTestsLegifrance(unittest.TestCase):
    def test_extract_articles_to_excel(self):
        url_du_sommaire = "https://www.legifrance.gouv.fr/affichCode.do?cidTexte=LEGITEXT000023983208&dateTexte=20200306"

        titre = "Code de l'énergie"

        # Request the content of a page from the url
        html = requests.get(url_du_sommaire)

        # Parse the content of html
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find_all("span", {"class": "codeLienArt"}) is not None:
            articles = soup.find_all("span", {"class": "codeLienArt"})

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(titre.replace(" ", "_") + '.xlsx')
            worksheet = workbook.add_worksheet("Articles")

            # Start from the first cell. Rows and columns are zero indexed.
            row = 0
            col = 0

            worksheet.write(row, col, "Articles")

            for article in articles:
                row += 1
                print(article.find("a").text)
                worksheet.write(row, col, article.find("a").text)

            workbook.close()

    
    def test_extract_text_of_one_article(self):
        print("test_text_of_one_article")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_of_one_article = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419280"

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_one_article, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        if soup.find('article') is not None:
            text = soup.find('article').text.replace('Versions', '').replace('Liens relatifs', '')
            print(text)
        else:
            print("no article")

    def test_extract_all_articles_from_one_code_in_force(self):
        print("test_extract_all_articles_from_one_code_in_force")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_of_one_code_in_force = "https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006070721"

        time.sleep(3)

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_one_code_in_force, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        if soup.find('a', {'class': 'articleLink'}) is not None:
            all_articles = soup.find_all('a', {'class': 'articleLink'})

            for article in all_articles:
                title = "Article " + article.get('data-na')
                link = "https://www.legifrance.gouv.fr/codes/article_lc/" + article.get('id').replace('art', '')
                print(title + " : " + link)
        else:
            print("no email type 1")

    def test_extract_text_of_one_law(self):
        print('test_extract_text_of_one_law')

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_of_one_law = "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000038029184?tab_selection=lawarticledecree&searchField=ALL&query=*&searchProximity=&searchType=ALL&isAdvancedResult=&isAdvancedResult=&dateSignature=&datePublication=&nature=LOI&typeRecherche=date&dateVersion=16%2F01%2F2021&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=2&tab_selection=lawarticledecree#lois"

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_one_law, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        title = ""
        text = ""

        if soup.find("h1", {'class': 'main-title'}) is not None:
            title += soup.find("h1", {'class': 'main-title'}).text
        else:
            print("no h1 class main-title")

        if soup.find("div", {'class': 'page-content'}) is not None:
            text += soup.find("div", {'class': 'page-content'}).text
        else:
            print("no div class page-content")

        print(title + " " + text)

    def test_extract_all_laws_from_one_search(self):
        print("test_extract_all_laws_from_one_search")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_of_all_laws_from_one_search = "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchProximity=&searchType=ALL&isAdvancedResult=&isAdvancedResult=&dateSignature=&datePublication=&nature=LOI&typeRecherche=date&dateVersion=16%2F01%2F2021&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=1&tab_selection=lawarticledecree#lois"

        time.sleep(3)

        # Request the content of a page from the url
        html_of_one_article = requests.get(url_of_all_laws_from_one_search, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

        number_of_pages = 0

        if soup.find("p", {"class": "nb-result head-filter-title"}) is not None:
            number_of_pages_with_coma = int(soup.find("p", {"class": "nb-result head-filter-title"})
                                            .text
                                            .replace(' résultat(s) trouvé(s)', '')
                                            ) / 100

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

            for i in range(1, number_of_pages + 1):
                url_of_one_page = "https://www.legifrance.gouv.fr/search/lois?tab_selection=lawarticledecree&searchField=ALL&query=*&searchProximity=&searchType=ALL&isAdvancedResult=&isAdvancedResult=&dateSignature=&datePublication=&nature=LOI&typeRecherche=date&dateVersion=16%2F01%2F2021&typePagination=DEFAUT&sortValue=SIGNATURE_DATE_DESC&pageSize=100&page=" + str(i) + "&tab_selection=lawarticledecree#lois"

                print(url_of_one_page)

                time.sleep(3)

                # Request the content of a page from the url
                html_of_one_article = requests.get(url_of_one_page, headers=headers)

                # Parse the content of html_doc
                soup = BeautifulSoup(html_of_one_article.content, 'html.parser')

                if soup.find("article", {"class": "result-item"}) is not None:
                    all_laws = soup.find_all("article", {"class": "result-item"})

                    for law in all_laws:
                        if law.find('h2', {'class': 'title-result-item'}) is not None:
                            title = law.find('h2', {'class': 'title-result-item'}).find('a').text
                            link = "https://www.legifrance.gouv.fr/loda/id/" + law.find('h2', {'class': 'title-result-item'}).get('data-id')
                            print(title + " " + link)
                        else:
                            print("no h2 title-result-item")
                else:
                    print("no article result-item")

        else:
            print("no pages at all")


if __name__ == '__main__':
    unittest.main()
