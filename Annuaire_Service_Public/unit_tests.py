import unittest
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time


class UnitTestsAnnuaireServicePublic(unittest.TestCase):
    def test_extract_nom(self):
        print("test_extract_nom")

        url_result = "https://lannuaire.service-public.fr/ile-de-france/yvelines/sous_pref-78361-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#contentTitle") is not None:
            print("title : " + soup.select_one("#contentTitle").text)

        else:
            print("no title")

    def test_extract_adresse_postale(self):
        print("test_extract_adresse_postale")

        url_result = "https://lannuaire.service-public.fr/ile-de-france/yvelines/sous_pref-78361-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#officialAddress") is not None:
            adresse_postale = soup.select_one("#officialAddress").text.replace("\n", " ").replace("Afficher la carte", "")

            print("adresse postale : " + adresse_postale)

        else:
            print("no adresse postale")

    def test_extract_telephone(self):
        print("test_extract_telephone")

        url_result = "https://lannuaire.service-public.fr/ile-de-france/yvelines/sous_pref-78361-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#contentPhone_1") is not None:
            telephone = soup.select_one("#contentPhone_1").text

            print("telephone : " + telephone)

        else:
            print("no telephone")

    def test_extract_site_internet(self):
        print("test_extract_site_internet")

        url_result = "https://lannuaire.service-public.fr/ile-de-france/yvelines/sous_pref-78361-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#websites") is not None:
            website = soup.select_one("#websites").text

            print("website : " + website)

        else:
            print("no website")

    def test_extract_mail(self):
        print("test_extract_mail")

        url_result = "https://lannuaire.service-public.fr/ile-de-france/yvelines/sous_pref-78361-01"

        # Request the content of a page from the url
        html = requests.get(url_result)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select_one("#contentContactEmail") is not None:
            content_contact_email = soup.select_one("#contentContactEmail").text\
                .replace("        Courriel : ", "")\
                .replace("      ", "")\
                .replace("\n", "")

            print("content_contact_email : " + content_contact_email)

        else:
            print("no content_contact_email")

    def test_extract_list_of_contacts_for_all_pages(self):
        print("test_extract_list_of_contacts_for_all_pages")

        url_list = "https://lannuaire.service-public.fr/recherche?where=ile%20de%20france&whoWhat=pr%C3%A9fecture&page="

        number_of_pages = 8

        i = 1

        for x in range(1, number_of_pages + 1):
            # Request the content of a page from the url
            html_list = requests.get(url_list)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html_list.content, 'html.parser')

            if soup.find("ul", {"class", "result-list"}) is not None:
                all_li = soup.find("ul", {"class", "result-list"}).find_all("li", {"class", "result-item"})

                for li in all_li:
                    lien = li.find("a").get("href")

                    html_lien = requests.get(lien)

                    time.sleep(3)

                    # Parse the content of html_doc
                    soup_lien = BeautifulSoup(html_lien.content, 'html.parser')

                    title = ""
                    adresse_postale = ""
                    telephone = ""
                    website = ""
                    content_contact_email = ""

                    if soup_lien.select_one("#contentTitle") is not None:
                        title += soup_lien.select_one("#contentTitle").text
                    else:
                        print(str(i) + " no title")

                    if soup_lien.select_one("#officialAddress") is not None:
                        adresse_postale += soup_lien.select_one("#officialAddress").text.replace("\n", " ").replace(
                            "Afficher la carte", "")
                    else:
                        print(str(i) + " no adresse postale")

                    if soup_lien.select_one("#contentPhone_1") is not None:
                        telephone += soup_lien.select_one("#contentPhone_1").text
                    else:
                        print(str(i) + " no telephone")

                    if soup_lien.select_one("#websites") is not None:
                        website += soup_lien.select_one("#websites").text
                    else:
                        print(str(i) + " no website")

                    if soup_lien.select_one("#contentContactEmail") is not None:
                        content_contact_email += "'" + soup_lien.select_one("#contentContactEmail").text\
                            .replace("        Courriel : ", "") \
                            .replace("      ", "") \
                            .replace("\n", "") + "',"
                    else:
                        print(str(i) + " no content_contact_email")

                    print(str(i) + " contact : "
                          + title + " / "
                          + adresse_postale + " / "
                          + telephone + " / "
                          + website + " / "
                          + content_contact_email)

                    i += 1

            else:
                print("no ul class result-list")

    def test_extract_contacts_for_excel_for_all_pages(self):
        print("test_extract_list_of_contacts_for_all_pages")

        url_list = "https://lannuaire.service-public.fr/recherche?where=ile%20de%20france&whoWhat=pr%C3%A9fecture&page="

        number_of_pages = 8

        i = 1

        contacts = []

        for x in range(1, number_of_pages + 1):
            # Request the content of a page from the url
            html_list = requests.get(url_list)

            time.sleep(2)

            # Parse the content of html_doc
            soup = BeautifulSoup(html_list.content, 'html.parser')

            if soup.find("ul", {"class", "result-list"}) is not None:
                all_li = soup.find("ul", {"class", "result-list"}).find_all("li", {"class", "result-item"})

                for li in all_li:
                    lien = li.find("a").get("href")

                    html_lien = requests.get(lien)

                    time.sleep(2)

                    # Parse the content of html_doc
                    soup_lien = BeautifulSoup(html_lien.content, 'html.parser')

                    title = ""
                    adresse_postale = ""
                    telephone = ""
                    website = ""
                    content_contact_email = ""

                    if soup_lien.select_one("#contentTitle") is not None:
                        title += soup_lien.select_one("#contentTitle").text
                    else:
                        print(str(i) + " no title")

                    if soup_lien.select_one("#officialAddress") is not None:
                        adresse_postale += soup_lien.select_one("#officialAddress").text.replace("\n", " ").replace(
                            "Afficher la carte", "")
                    else:
                        print(str(i) + " no adresse postale")

                    if soup_lien.select_one("#contentPhone_1") is not None:
                        telephone += soup_lien.select_one("#contentPhone_1").text
                    else:
                        print(str(i) + " no telephone")

                    if soup_lien.select_one("#websites") is not None:
                        website += soup_lien.select_one("#websites").text
                    else:
                        print(str(i) + " no website")

                    if soup_lien.select_one("#contentContactEmail") is not None:
                        content_contact_email += "'" + soup_lien.select_one("#contentContactEmail").text\
                            .replace("        Courriel : ", "") \
                            .replace("      ", "") \
                            .replace("\n", "") + "',"
                    else:
                        print(str(i) + " no content_contact_email")

                    print(str(i) + " contact : "
                          + title + " / "
                          + adresse_postale + " / "
                          + telephone + " / "
                          + website + " / "
                          + content_contact_email)

                    contact = {
                        "title": title,
                        "adresse_postale": adresse_postale,
                        "telephone": telephone,
                        "website": website,
                        "content_contact_email": content_contact_email
                    }

                    contacts.append(contact)

                    i += 1

            else:
                print("no ul class result-list")

        # Create a workbook and add a worksheet
        workbook = xlsxwriter.Workbook('a_s_p_pref_i_d_f.xlsx')
        worksheet = workbook.add_worksheet('data')

        worksheet.write(0, 0, 'title')
        worksheet.write(0, 1, 'adresse_postale')
        worksheet.write(0, 2, 'telephone')
        worksheet.write(0, 3, 'website')
        worksheet.write(0, 4, 'content_contact_email')

        row = 1

        for one_contact in contacts:
            # title
            worksheet.write(row, 0, one_contact.get('title'))

            # adresse_postale
            worksheet.write(row, 1, one_contact.get('adresse_postale'))

            # telephone
            worksheet.write(row, 2, one_contact.get('telephone'))

            # website
            worksheet.write(row, 3, one_contact.get('website'))

            # content_contact_email
            worksheet.write(row, 4, one_contact.get('content_contact_email'))

            row += 1

        workbook.close()

    def test_xlsxwriter(self):
        print("test_xlsxwriter")

        workbook = xlsxwriter.Workbook('hello.xlsx')
        worksheet = workbook.add_worksheet('data')

        worksheet.write('A1', 'Hello world')

        workbook.close()


if __name__ == '__main__':
    unittest.main()
