from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesCanada(unittest.TestCase):
    def test_extract_one_email(self):
        try:
            url = "https://www.pagesjaunes.ca/bus/Quebec/Montreal/Hilton/6981682.html?what=hotel&where=Montreal+QC&useContext=true"

            # Request the content of a page from the url
            html = requests.get(url)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            try:
                if soup.find("li", {"class": "mlr__item--website"}) is not None:
                    try:
                        if soup\
                                .find("li", {"class": "mlr__item--website"})\
                                .find("a", {"class": "mlr__item__cta"}) is not None:
                            raw_website = soup\
                                .find("li", {"class": "mlr__item--website"})\
                                .find("a", {"class": "mlr__item__cta"})\
                                .get("href")

                            email = "info@" + raw_website.split('?redirect=')[1]\
                                .replace('http%3A%2F%2F', '')\
                                .split('%2F')[0]

                            print('email : ' + email)
                        else:
                            print("no a class mlr__item__cta")
                    except Exception as e:
                        print("error a mlr__item__cta  hide-print : " + str(e))
                else:
                    print("no li class mlr__item--website")
            except Exception as e:
                print ("error li mlr__item--website : " + str(e))
        except Exception as e:
            print("error url : " + str(e))

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        try:
            activity = "hotel"
            city = "Montreal+QC"
            url_search = "https://www.pagesjaunes.ca/search/si/1/" + activity + "/" + city
            html_search = requests.get(url_search)
            soup_search = BeautifulSoup(html_search.content, 'html.parser')

            number_of_pages = 0

            # find the number of pages
            try:
                if soup_search.find("span", {"class": "pageCount"}) is not None:
                    try:
                        if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                            number_of_pages += int(soup_search
                                                   .find("span", {"class": "pageCount"})
                                                   .find_all("span")[1]
                                                   .text)
                            print("number_of_pages : " + str(number_of_pages))
                        else:
                            print("no span")
                    except Exception as e:
                        print("error span : " + str(e))
                else:
                    print("no span class pageCount")
            except Exception as e:
                print("error span class pageCount : " + str(e))

            i_1 = 0

            for i in range(1, number_of_pages + 1):
                try:
                    url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                 + str(i) + "/" \
                                                 + activity + "/" \
                                                 + city

                    print(url_of_one_page_of_results)

                    time.sleep(2)

                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                'html.parser')

                    try:
                        if soup_of_one_page_of_results\
                                .find("div", {"class": "resultList"}) is not None:
                            try:
                                if soup_of_one_page_of_results\
                                        .find("div", {"class": "resultList"})\
                                        .find("div", {"class": "listing"}) is not None:

                                    all_listing = soup_of_one_page_of_results\
                                        .find("div", {"class": "resultList"})\
                                        .find_all("div", {"class": "listing"})

                                    for listing in all_listing:
                                        i_1 += 1

                                        try:
                                            if listing.find("a", {"class": "listing__name--link"}) is not None:
                                                website = "https://www.pagesjaunes.ca" + listing\
                                                    .find("a", {"class": "listing__name--link"})\
                                                    .get("href")

                                                try:
                                                    url = website

                                                    time.sleep(2)

                                                    # Request the content of a page from the url
                                                    html = requests.get(url)

                                                    # Parse the content of html_doc
                                                    soup = BeautifulSoup(html.content, 'html.parser')

                                                    try:
                                                        if soup.find("li", {"class": "mlr__item--website"}) is not None:
                                                            try:
                                                                if soup \
                                                                        .find("li", {"class": "mlr__item--website"}) \
                                                                        .find("a",
                                                                              {"class": "mlr__item__cta"}) is not None:
                                                                    raw_website = soup \
                                                                        .find("li", {"class": "mlr__item--website"}) \
                                                                        .find("a", {"class": "mlr__item__cta"}) \
                                                                        .get("href")

                                                                    email = "info@" + raw_website\
                                                                        .split('?redirect=')[1]\
                                                                        .replace('http%3A%2F%2F', '')\
                                                                        .split('%2F')[0]\
                                                                        .replace("www.", "")

                                                                    try:
                                                                        if validate_email(email, verify=True) != False:
                                                                            print(str(i_1) + " The email : " + str(
                                                                                email) + " does exist.")
                                                                        else:
                                                                            print(str(i_1) + " The email : " + str(
                                                                                email) + " doesn't exist.")
                                                                    except Exception as e:
                                                                        print(str(i_1) + " error validate_email : "
                                                                              + str(e))
                                                                else:
                                                                    print("no a class mlr__item__cta")
                                                            except Exception as e:
                                                                print("error a mlr__item__cta  hide-print : " + str(e))
                                                        else:
                                                            print("no li class mlr__item--website")
                                                    except Exception as e:
                                                        print("error li mlr__item--website : " + str(e))
                                                except Exception as e:
                                                    print("error url : " + str(e))
                                            else:
                                                print("")
                                        except Exception as e:
                                            print("no a class listing__name--link")
                                else:
                                    print("no listing")
                            except Exception as e:
                                print("error  : ")
                        else:
                            print("no resultList")
                    except Exception as e:
                        print("error div class resultList : " + str(e))
                except Exception as e:
                    print("error url_of_one_page_of_results : " + str(e))
        except Exception as e:
            print("error url_search : " + str(e))

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        try:
            activites = [
                # {'id': '1', 'url': 'agence+de+placement'},
                # {'id': '2', 'url': 'agence+immobilière'},
                # {'id': '3', 'url': "recrutement"},
                # {'id': '4', 'url': 'logiciel'},
                # {'id': '5', 'url': 'hotel'},
                # {'id': '6', 'url': 'social'},
                # {'id': '7', 'url': 'nettoyage'},
                # {'id': '8', 'url': 'association'},
                # {'id': '9', 'url': 'etablissement+financier'},
                # {'id': '10', 'url': 'restaurant'},
                # {'id': '11', 'url': 'batiment'},
                # {'id': '12', 'url': 'coiffeur'},
                # {'id': '13', 'url': 'fleuriste'},
                # {'id': '14', 'url': 'serrurier'},
                # {'id': '15', 'url': 'boulangerie'},
                # {'id': '16', 'url': 'assurance'},
                # {'id': '17', 'url': 'pharmacie'},
                # {'id': '18', 'url': 'demenagement'},
                # {'id': '19', 'url': 'electricite'},
                # {'id': '20', 'url': 'plomberie'},
                # {'id': '21', 'url': 'securite'},
                # {'id': '22', 'url': 'avocat'},
                # {'id': '23', 'url': 'banque'},
                # {'id': '24', 'url': 'garage'},
                # {'id': '25', 'url': 'dentiste'},
                # {'id': '26', 'url': 'docteur'},
                # {'id': '27', 'url': 'comptable'},
                # {'id': '28', 'url': 'supermarche'},
                # {'id': '29', 'url': 'notaire'},
                # {'id': '30', 'url': 'bijoutier'},
                # {'id': '31', 'url': 'couturier'},
                # {'id': '32', 'url': 'boucherie'},
                # {'id': '33', 'url': 'librairie'},
                # {'id': '34', 'url': 'architecte'}
                {'id': '36', 'url': 'ciment'},
                {'id': '37', 'url': 'chauffage'},
                {'id': '38', 'url': 'bateau'},
                {'id': '39', 'url': 'climatisation'},
                {'id': '41', 'url': 'acier'},
                {'id': '42', 'url': 'produits+chimiques'},
                {'id': '43', 'url': 'gaz'},
                {'id': '44', 'url': 'achat+or'}
            ]

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB'}, #edmonton
                {'id': '474', 'nom': 'Victoria+BC'}, #victoria
                {'id': '475', 'nom': 'Winnipeg+MB'}, #winnipeg
                {'id': '476', 'nom': 'Fredericton+NB'}, #fredericton
                {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL'}, #saint john
                {'id': '478', 'nom': 'Halifax+NS'}, #halifax
                {'id': '479', 'nom': 'Yellowknife+NT'}, #yellowknife
                {'id': '480', 'nom': 'Iqaluit+NU'}, #iqaluit
                {'id': '481', 'nom': 'Toronto+ON'}, #toronto
                {'id': '482', 'nom': 'Charlottetown+PE'}, #charlottetown
                {'id': '483', 'nom': 'Quebec+QC'}, #quebec
                {'id': '484', 'nom': 'Regina+SK'}, #regina
                {'id': '485', 'nom': 'Whitehorse+YT'} #whitehorse
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        city = capitale.get('nom')

                        url_search = "https://www.pagesjaunes.ca/search/si/1/" \
                                     + activity + "/" + city

                        html_search = requests.get(url_search)

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        i_1 = 0

                        for i in range(1, number_of_pages + 1):
                            try:
                                url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                             + str(i) + "/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(2)

                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    i_1 += 1

                                                    try:
                                                        if listing.find("a",
                                                                        {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.pagesjaunes.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url = website

                                                                time.sleep(2)

                                                                # Request the content of a page from the url
                                                                html = requests.get(url)

                                                                # Parse the content of html_doc
                                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                                try:
                                                                    if soup.find("li", {
                                                                        "class": "mlr__item--website"}) is not None:
                                                                        try:
                                                                            if soup \
                                                                                    .find("li", {
                                                                                "class": "mlr__item--website"}) \
                                                                                    .find("a",
                                                                                          {
                                                                                              "class": "mlr__item__cta"}) is not None:
                                                                                raw_website = soup \
                                                                                    .find("li", {
                                                                                    "class": "mlr__item--website"}) \
                                                                                    .find("a",
                                                                                          {"class": "mlr__item__cta"}) \
                                                                                    .get("href")

                                                                                email = "info@" + raw_website \
                                                                                    .split('?redirect=')[1] \
                                                                                    .replace('http%3A%2F%2F', '') \
                                                                                    .replace('https%3A%2F%2F', '') \
                                                                                    .split('%2F')[0] \
                                                                                    .replace("www.", "")

                                                                                try:
                                                                                    connection = pymysql.connect(
                                                                                        host='localhost',
                                                                                        port=3306,
                                                                                        user='',
                                                                                        password='',
                                                                                        db='contacts_professionnels',
                                                                                        charset='utf8mb4',
                                                                                        cursorclass=pymysql.cursors.DictCursor
                                                                                    )

                                                                                    with connection.cursor() as cursor:
                                                                                        try:
                                                                                            sql = "INSERT INTO `emails` (" \
                                                                                                  "`id_activite`, " \
                                                                                                  "`id_capitale_du_monde`, " \
                                                                                                  "`email`) VALUE (%s, %s, %s)"
                                                                                            cursor.execute(
                                                                                                sql, (
                                                                                                    activite.get(
                                                                                                        'id'),
                                                                                                    capitale.get(
                                                                                                        'id'),
                                                                                                    email))
                                                                                            connection.commit()
                                                                                            print(str(
                                                                                                i_1) + " The record is stored : " + str(
                                                                                                email))
                                                                                            connection.close()
                                                                                        except Exception as e:
                                                                                            print(str(i_1)
                                                                                                  + " The record already exists : "
                                                                                                  + str(email)
                                                                                                  + " - "
                                                                                                  + str(e))
                                                                                            connection.close()
                                                                                except Exception as e:
                                                                                    print(str(i_1)
                                                                                          + " error validate_email : "
                                                                                          + str(e))
                                                                            else:
                                                                                print("no a class mlr__item__cta")
                                                                        except Exception as e:
                                                                            print(
                                                                                "error a mlr__item__cta  hide-print : " + str(
                                                                                    e))
                                                                    else:
                                                                        print("no li class mlr__item--website")
                                                                except Exception as e:
                                                                    print("error li mlr__item--website : " + str(e))
                                                            except Exception as e:
                                                                print("error url : " + str(e))
                                                        else:
                                                            print("")
                                                    except Exception as e:
                                                        print("no a class listing__name--link " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')

    def test_extract_all_url_message_from_all_page_of_results_for_all_capitals_and_one_activity(self):
        print("test_extract_all_url_message_from_all_page_of_results_for_all_capitals_and_one_activity")

        try:
            location = "Edmonton+AB"
            start = 1
            number_of_pages = 20

            i_1 = 1

            for i in range(start, number_of_pages+1):
                url_page_results = "https://www.yellowpages.ca/search/si/" + str(i) + "/car+repair/" + location

                print("url_page_results : " + url_page_results)

                html_search = requests.get(url_page_results)

                soup_search = BeautifulSoup(html_search.content, 'html.parser')

                if soup_search.find("div", {"class": "resultList"}) is not None:
                    if soup_search.find("div", {"class": "resultList"}).find("div", {"class": "listing"}) is not None:
                        results = soup_search.find("div", {"class": "resultList"}).find_all("div", {"class": "listing"})

                        for result in results:
                            if result.find("li", {"class": "mlr__item--message"}) is not None:
                                url_page = "https://www.yellowpages.ca" + result.find("link", {"itemprop": "url"}).get("href")
                                print("url_page " + str(i_1) + " : " + url_page)
                            else:
                                print(str(i_1) + " div class mlr__item--message is not present")

                            i_1 += 1
                    else:
                        print("div class listing is not present")
                else:
                    print("div class resultList is not present")
        except Exception as e:
            print("error : " + str(e))


if __name__ == '__main__':
    unittest.main()
