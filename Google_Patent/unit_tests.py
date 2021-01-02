import unittest
import time
from bs4 import BeautifulSoup
import requests
import xlsxwriter


class UnitTestsDataMiningGooglePatent(unittest.TestCase):
    def test_mining_title_from_one_patent(self):
        print("test_mining_title_from_one_patent")

        # url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        url_for_one_patent = "https://patents.google.com/patent/GB191026356A/en?q=transmutation&before=priority:19900101&page=1"

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        time.sleep(3)

        # print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("span", {"itemprop": "title"}) is not None:
            print("Title : " + soup.find("span", {"itemprop": "title"}).text)

    def test_mining_patent_number_from_one_patent(self):
        print("test_mining_patent_number_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        time.sleep(3)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("dd", {"itemprop": "publicationNumber"}) is not None:
            print("Patent number : " + soup.find("dd", {"itemprop": "publicationNumber"}).text)

    def test_mining_inventor_from_one_patent(self):
        print("test_mining_inventor_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("dd", {"itemprop": "inventor"}) is not None:
            print("Inventor : " + soup.find("dd", {"itemprop": "inventor"}).text)

    def test_mining_abstract_text_from_one_patent(self):
        print("test_mining_abstract_text_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("div", {"itemprop": "content"}) is not None:
            print("Abstract text : " + soup.find("div", {"itemprop": "content"}).text.replace("\n", ""))

    def test_mining_images_urls_from_one_patent(self):
        print("test_mining_images_urls_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("img", {"itemprop": "thumbnail"}) is not None:
            images_url_list = []
            image_urls = soup.find_all("img", {"itemprop": "thumbnail"})

            for image_url in image_urls:
                images_url_list.append(image_url.get('src'))

            i = 0

            for image_url in images_url_list:
                i += 1
                print("Image url " + str(i) + " : " + image_url)

    def test_mining_pdf_url_from_one_patent(self):
        print("test_mining_pdf_file_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("a", {"itemprop": "pdfLink"}) is not None:
            print("PDF url : " + soup.find("a", {"itemprop": "pdfLink"}).get('href'))

    def test_mining_classifications_from_one_patent(self):
        print("test_mining_classifications_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("li", {"itemprop": "cpcs"}) is not None:
            classification_list = soup.find_all("li", {"itemprop": "cpcs"})

            for classification in classification_list:
                i += 1
                print("Classificaton " + str(i) + " : " + classification.text.replace("\n", ""))

    def test_mining_description_text_from_one_patent(self):
        print("test_mining_description_text_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("section", {"itemprop": "description"}) is not None:
            paragraphes = soup.find("section", {"itemprop": "description"}).find_all('p')

            for paragraphe in paragraphes:
                print(paragraphe.text)

    def test_mining_claims_text_from_one_patent(self):
        print("test_mining_claims_text_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("section", {"itemprop": "claims"}) is not None:
            claims = soup.find("section", {"itemprop": "claims"}).find_all("div", {"class": "claim-text"})

            for claim in claims:
                print(claim.text)

    def test_mining_patent_citations_list_from_one_patent(self):
        print("test_mining_patent_citations_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "backwardReferences"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "backwardReferences"})

            for tr in all_tr:
                i += 1

                publication_number = tr.find("span", {"itemprop": "publicationNumber"}).text
                priority_date = tr.find("td", {"itemprop": "priorityDate"}).text
                publication_date = tr.find("td", {"itemprop": "publicationDate"}).text
                assignee = tr.find("span", {"itemprop": "assigneeOriginal"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                url_patent_citation = "https://patents.google.com" + tr.find("span", {"itemprop": "publicationNumber"}).parent.get('href')

                print("Patent citation " + str(i) + " : "
                      + publication_number + " / "
                      + url_patent_citation + " / "
                      + priority_date + " / "
                      + publication_date + " / "
                      + assignee + " / "
                      + title)

    def test_mining_non_patent_citations_list_from_one_patent(self):
        print("test_mining_non_patent_citations_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "detailedNonPatentLiterature"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "detailedNonPatentLiterature"})

            for tr in all_tr:
                i += 1
                print("Non-Patent Citation " + str(i) + " : " + tr.find("span", {"itemprop": "title"}).text)

    def test_mining_cited_by_list_from_one_patent(self):
        print("test_mining_cited_by_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "forwardReferencesOrig"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "forwardReferencesOrig"})

            for tr in all_tr:
                i += 1

                publication_number = tr.find("span", {"itemprop": "publicationNumber"}).text
                priority_date = tr.find("td", {"itemprop": "priorityDate"}).text
                publication_date = tr.find("td", {"itemprop": "publicationDate"}).text
                assignee = tr.find("span", {"itemprop": "assigneeOriginal"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                url_cited_by = "https://patents.google.com" + tr.find("span", {"itemprop": "publicationNumber"}).parent.get('href')

                print("Cited by " + str(i) + " : "
                      + publication_number + " / "
                      + url_cited_by + " / "
                      + priority_date + " / "
                      + publication_date + " / "
                      + assignee + " / "
                      + title)

    def test_mining_similar_documents_list_from_one_patent(self):
        print("test_mining_similar_documents_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "similarDocuments"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "similarDocuments"})

            for tr in all_tr:
                i += 1

                if tr.find("span", {"itemprop": "scholarAuthors"}) is not None:
                    publication = tr.find("span", {"itemprop": "scholarAuthors"}).text
                    publication_date = tr.find("time", {"itemprop": "publicationDate"}).text
                    title = tr.find("td", {"itemprop": "title"}).text
                    url_similar_documents = "https://patents.google.com" + tr.find("span", {"itemprop": "scholarAuthors"}).parent.get('href')

                    print("Similar Documents " + str(i) + " : "
                          + publication + " / "
                          + url_similar_documents + " / "
                          + publication_date + " / "
                          + title)
                else:
                    publication = tr.find("span", {"itemprop": "publicationNumber"}).text
                    publication_date = tr.find("time", {"itemprop": "publicationDate"}).text
                    title = tr.find("td", {"itemprop": "title"}).text
                    url_similar_documents = "https://patents.google.com" + tr.find("span", {"itemprop": "publicationNumber"}).parent.get('href')

                    print("Similar Documents " + str(i) + " : "
                          + publication + " / "
                          + url_similar_documents + " / "
                          + publication_date + " / "
                          + title)

    def test_mining_parent_applications_list_from_one_patent(self):
        print("test_mining_parent_applications_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "parentApps"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "parentApps"})

            for tr in all_tr:
                i += 1

                application = tr.find("span", {"itemprop": "applicationNumber"}).text
                representative_publication = tr.find("span", {"itemprop": "representativePublication"}).text
                priority_date = tr.find("td", {"itemprop": "priorityDate"}).text
                filing_date = tr.find("td", {"itemprop": "filingDate"}).text
                relation = tr.find("span", {"itemprop": "relationType"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                url_parent_applications = "https://patents.google.com" + tr.find("span", {"itemprop": "representativePublication"}).parent.get('href')

                print("Parent Applications " + str(i) + " : "
                      + application + " / "
                      + representative_publication + " / "
                      + url_parent_applications + " / "
                      + priority_date + " / "
                      + filing_date + " / "
                      + relation + " / "
                      + title)

    def test_mining_priority_applications_list_from_one_patent(self):
        print("test_mining_priority_applications_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "priorityApps"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "priorityApps"})

            for tr in all_tr:
                i += 1

                application = tr.find("span", {"itemprop": "applicationNumber"}).text
                representative_publication = tr.find("span", {"itemprop": "representativePublication"}).text
                priority_date = tr.find("td", {"itemprop": "priorityDate"}).text
                filing_date = tr.find("td", {"itemprop": "filingDate"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                url_representative_publication = "https://patents.google.com" + tr.find("span", {
                    "itemprop": "representativePublication"}).parent.get('href')

                print("Priority Applications " + str(i) + " : "
                      + application + " / "
                      + representative_publication + " / "
                      + url_representative_publication + " / "
                      + priority_date + " / "
                      + filing_date + " / "
                      + title)

    def test_mining_applications_claiming_priority_list_from_one_patent(self):
        print("test_mining_applications_claiming_priority_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "appsClaimingPriority"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "appsClaimingPriority"})

            for tr in all_tr:
                i += 1

                application = tr.find("span", {"itemprop": "applicationNumber"}).text

                representative_publication = tr.find("span", {"itemprop": "representativePublication"}).text

                priority_date = tr.find("td", {"itemprop": "priorityDate"}).text

                filing_date = tr.find("td", {"itemprop": "filingDate"}).text

                title = tr.find("td", {"itemprop": "title"}).text

                url_representative_publication = "https://patents.google.com" + tr.find("span", {
                    "itemprop": "representativePublication"}).parent.get('href')

                print("Applications Claiming Priority " + str(i) + " : "
                      + application + " / "
                      + representative_publication + " / "
                      + url_representative_publication + " / "
                      + priority_date + " / "
                      + filing_date + " / "
                      + title)

    def test_legal_events_list_from_one_patent(self):
        print("test_legal_events_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "legalEvents"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "legalEvents"})

            for tr in all_tr:
                i += 1

                date = tr.find("time", {"itemprop": "date"}).text
                code = tr.find("td", {"itemprop": "code"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                attributes = tr.find_all("p", {"itemprop": "attributes"})

                description = ""

                for attribute in attributes:
                    description += " " + attribute.text.replace("\n", "")

                print("Legal Events " + str(i) + " : "
                      + date + " / "
                      + code + " / "
                      + title + " / "
                      + description)

    def test_concepts_list_from_one_patent(self):
        print("test_concepts_list_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        i = 0

        if soup.find("tr", {"itemprop": "legalEvents"}) is not None:
            all_tr = soup.find_all("tr", {"itemprop": "legalEvents"})

            for tr in all_tr:
                i += 1

                date = tr.find("time", {"itemprop": "date"}).text
                code = tr.find("td", {"itemprop": "code"}).text
                title = tr.find("td", {"itemprop": "title"}).text
                attributes = tr.find_all("p", {"itemprop": "attributes"})

                description = ""

                for attribute in attributes:
                    description += " " + attribute.text.replace("\n", "")

                print("Legal Events " + str(i) + " : "
                      + date + " / "
                      + code + " / "
                      + title + " / "
                      + description)

    def test_mining_current_assignee_from_one_patent(self):
        print("test_mining_current_assignee_from_one_patent")

        url_for_one_patent = 'https://patents.google.com/patent/US5149407?oq=stanley+meyer'

        # Request the content of a page from the url
        html = requests.get(url_for_one_patent)

        print(html.text)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.text, 'html.parser')

        if soup.find("dd", {"itemprop": "assigneeCurrent"}) is not None:
            print("Current Assignee : " + soup.find("dd", {"itemprop": "assigneeCurrent"}).text.replace("\n", ""))

    def test_export_excel_file_for_transmutation_reactors(self):
        print("test_export_excel_file_for_transmutation_reactors")

        workbook = xlsxwriter.Workbook('patents_transmutation_reactors.xlsx')
        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, "Title")
        worksheet.write(0, 1, "Link")
        worksheet.write(0, 2, "Patent number")

        row = 1

        for i in range(1, 2):
            url_page_of_results = "https://patents.google.com/?q=transmutation&page=" + str(i)
            print(url_page_of_results)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
            }

            html_page_of_results = requests.get(url_page_of_results, headers=headers)

            time.sleep(3)

            print(html_page_of_results.text)

            soup_page_of_results = BeautifulSoup(html_page_of_results.text, 'html.parser')

            if soup_page_of_results.find("search-result-item", {"class": "search-result-item"}) is not None:
                items = soup_page_of_results.find_all("search-result-item", {"class": "search-result-item"})

                for item in items:
                    title = item.select_one("#htmlContent").text

                    if "transmutation" in title:
                        url_page_of_result = "https://patents.google.com" + item.select_one("#link").get('href')

                        print(str(row) + " - " + url_page_of_result)

                        html_page_of_result = requests.get(url_page_of_result)

                        soup_page_of_result = BeautifulSoup(html_page_of_result.text, 'html.parser')

                        worksheet.write(row, 0, title)
                        worksheet.write(row, 1, url_page_of_result)

                        if soup_page_of_result.find("dd", {"itemprop": "publicationNumber"}) is not None:
                            patent_number = soup_page_of_result.find("dd", {"itemprop": "publicationNumber"}).text
                            worksheet.write(row, 2, patent_number)
                        else:
                            print("no publicationNumber")
                    else:
                        print("transmutation not present in the title")

                    row += 1
            else:
                print("no results")

        workbook.close()


if __name__ == '__main__':
    unittest.main()
