import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter


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


if __name__ == '__main__':
    unittest.main()
