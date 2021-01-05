import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesGuernesey(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.theguernseydirectory.com/guernsey/king-balti-indian-restaurant-takeaway/profile"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        try:
            if soup.find("address", {"itemprop": "address"}) is not None:
                try:
                    if soup\
                            .find("address", {"itemprop": "address"})\
                            .find("a", {"class": "email-address"}) is not None:
                        email = "info@" + soup\
                            .find("address", {"itemprop": "address"}) \
                            .find("a", {"class": "email-address"})\
                            .text\
                            .split("@")[1]

                        try:
                            print("1 - The email : " + email + " does exist.")
                        except Exception as e:
                            print(str(e))
                except Exception as e:
                    print(str(e))

                try:
                    if soup\
                            .find("address", {"itemprop": "address"})\
                            .find("a", {"target": "_blank"}) is not None:
                        email = "info@" + soup\
                            .find("address", {"itemprop": "address"}) \
                            .find("a", {"target": "_blank"})\
                            .text\
                            .replace("www.", "") \
                            .replace("http://www.", "") \
                            .replace("https://www.", "") \
                            .replace("http://", "") \
                            .replace("https://", "") \
                            .replace("/", "")

                        try:
                            print("2 - The email : " + email + " does exist.")
                        except Exception as e:
                            print(str(e))
                except Exception as e:
                    print(str(e))
            else:
                print('no email business')
        except Exception as e:
            print(str(e))

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "hotel"
        url_search = "https://www.theguernseydirectory.com/guernsey/" + activity + "/"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        try:
            if soup_search\
                    .find("span", {"class": "company-search"})\
                    .find("h1") is not None:
                number_of_pages_with_coma = int(
                    soup_search
                    .find("span", {"class": "company-search"})
                    .find("h1")
                    .text
                    .lower()
                    .replace(" found in Guernsey", "")
                    .split(" ")[0]
                )/15

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))

                i_1 = 0

                for i in range(1, number_of_pages+1):
                    url_of_one_page_of_results = url_search + "pageno=" + str(i)
                    print(url_of_one_page_of_results)
                    time.sleep(2)
                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                    try:
                        if soup_of_one_page_of_results\
                                .find("div", {"class": "listingpage"})\
                                .find("div", {"class": "listing"}) is not None:
                            for result_item in soup_of_one_page_of_results.find("div", {"class": "listingpage"})\
                                    .find_all("div", {"class": "listing"}):
                                i_1 += 1

                                url_result = "https://www.theguernseydirectory.com" + \
                                             result_item\
                                             .find("div", {"class": "listing-content"})\
                                             .find("h2", {"class": "h4"})\
                                             .find("a").get("href")

                                # Request the content of a page from the url
                                html = requests.get(url_result)

                                # Parse the content of html_doc
                                soup = BeautifulSoup(html.content, 'html.parser')

                                try:
                                    if soup.find("address", {"itemprop": "address"}) is not None:
                                        try:
                                            if soup \
                                                    .find("address", {"itemprop": "address"}) \
                                                    .find("a", {"class": "email-address"}) is not None:
                                                email = "info@" + soup \
                                                    .find("address", {"itemprop": "address"}) \
                                                    .find("a", {"class": "email-address"}) \
                                                    .text \
                                                    .split("@")[1]

                                                try:
                                                    print(str(i_1) + " The email : " + email + " does exist.")
                                                except Exception as e:
                                                    print(str(e))
                                            else:
                                                print(str(i_1) + " no email-address")

                                            if soup\
                                                    .find("address", {"itemprop": "address"}) \
                                                    .find("a", {"target": "_blank"}) is not None:
                                                email = "info@" + soup \
                                                    .find("address", {"itemprop": "address"}) \
                                                    .find("a", {"target": "_blank"}) \
                                                    .text \
                                                    .replace("www.", "") \
                                                    .replace("http://www.", "") \
                                                    .replace("https://www.", "") \
                                                    .replace("http://", "") \
                                                    .replace("https://", "") \
                                                    .replace("/", "")

                                                try:
                                                    print(str(i_1) + " The email : " + email + " does exist.")
                                                except Exception as e:
                                                    print(str(e))
                                            else:
                                                print(str(i_1) + " no _blank")
                                        except Exception as e:
                                            print(str(e))
                                    else:
                                        print(str(i_1) + " no email business")
                                except Exception as e:
                                    print(str(e))
                        else:
                            print("sorry there is no results")
                    except Exception as e:
                        print(str(e))
        except Exception as e:
            print(str(e))

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'labour'},
            # {'id': '2', 'url': 'estate-agents'}
            # {'id': '3', 'url': 'recruiter'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'landlord'},
            # {'id': '7', 'url': 'cleaning'},
            # {'id': '8', 'url': 'association'},
            # {'id': '9', 'url': 'financial'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'building'},
            # {'id': '12', 'url': 'hairdresser'},
            # {'id': '13', 'url': 'florist'},
            # {'id': '14', 'url': 'locksmith'},
            # {'id': '15', 'url': 'bakery'},
            # {'id': '16', 'url': 'insurance'},
            # {'id': '17', 'url': 'pharmacy'},
            # {'id': '18', 'url': 'mover'},
            # {'id': '19', 'url': 'electricity'},
            # {'id': '20', 'url': 'plumbing'},
            # {'id': '21', 'url': 'security'},
            # {'id': '22', 'url': 'lawyer'},
            # {'id': '23', 'url': 'bank'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'dentist'},
            # {'id': '26', 'url': 'doctor'},
            # {'id': '27', 'url': 'accounting'},
            # {'id': '28', 'url': 'supermarket'},
            # {'id': '29', 'url': 'notary'},
            # {'id': '30', 'url': 'jeweller'},
            # {'id': '31', 'url': 'tailor'},
            # {'id': '32', 'url': 'butcher'},
            # {'id': '33', 'url': 'library'},
            # {'id': '34', 'url': 'architect'},
            {'id': '36', 'url': 'cement'},
            {'id': '37', 'url': 'heating'},
            {'id': '38', 'url': 'boat'},
            {'id': '39', 'url': 'cold'},
            {'id': '41', 'url': 'steel'},
            {'id': '42', 'url': 'chemicals'},
            {'id': '43', 'url': 'gas'},
            {'id': '44', 'url': 'goldsmiths'}
        ]

        capitales_du_monde = [
            {'id': '279', 'nom': 'guernsey'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")

                        url_search = "https://www.theguernseydirectory.com/" + city + "/" + activity + "/"
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        try:
                            if soup_search \
                                    .find("span", {"class": "company-search"}) \
                                    .find("h1") is not None:
                                number_of_pages_with_coma = int(
                                    soup_search
                                    .find("span", {"class": "company-search"})
                                    .find("h1")
                                    .text
                                    .lower()
                                    .replace(" found in Guernsey", "")
                                    .split(" ")[0]
                                ) / 15

                                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                    number_of_pages += round(number_of_pages_with_coma) + 1
                                    print('number_of_pages : ' + str(number_of_pages))

                                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                    number_of_pages += round(number_of_pages_with_coma)
                                    print('number_of_pages : ' + str(number_of_pages))

                                i_1 = 0

                                for i in range(1, number_of_pages + 1):
                                    url_of_one_page_of_results = url_search + "pageno=" + str(i)
                                    print(url_of_one_page_of_results)
                                    time.sleep(2)
                                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "listingpage"}) \
                                                .find("div", {"class": "listing"}) is not None:
                                            for result_item in soup_of_one_page_of_results.find("div", {
                                                "class": "listingpage"}) \
                                                    .find_all("div", {"class": "listing"}):
                                                i_1 += 1

                                                url_result = "https://www.theguernseydirectory.com" + \
                                                             result_item \
                                                             .find("div", {"class": "listing-content"}) \
                                                             .find("h2", {"class": "h4"}) \
                                                             .find("a").get("href")

                                                # Request the content of a page from the url
                                                html = requests.get(url_result)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                try:
                                                    if soup.find("address", {"itemprop": "address"}) is not None:
                                                        try:
                                                            if soup \
                                                                    .find("address", {"itemprop": "address"}) \
                                                                    .find("a", {"class": "email-address"}) is not None:
                                                                email = "info@" + soup \
                                                                    .find("address", {"itemprop": "address"}) \
                                                                    .find("a", {"class": "email-address"}) \
                                                                    .text \
                                                                    .split("@")[1]

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
                                                                            cursor.execute(sql, (
                                                                                activite.get('id'),
                                                                                capitale.get('id'),
                                                                                email))
                                                                            connection.commit()
                                                                            print(str(i_1) +
                                                                                  " The record is stored : "
                                                                                  + str(email))
                                                                            connection.close()
                                                                        except Exception as e:
                                                                            print(str(i_1) +
                                                                                  " The record already exists : "
                                                                                  + str(email) + " " + str(e))
                                                                            connection.close()
                                                                except Exception as e:
                                                                    print(str(e))
                                                            else:
                                                                print(str(i_1) + " no email-address")

                                                            if soup \
                                                                    .find("address", {"itemprop": "address"}) \
                                                                    .find("a", {"target": "_blank"}) is not None:
                                                                email = "info@" + soup \
                                                                    .find("address", {"itemprop": "address"}) \
                                                                    .find("a", {"target": "_blank"}) \
                                                                    .text \
                                                                    .replace("www.", "") \
                                                                    .replace("http://www.", "") \
                                                                    .replace("https://www.", "") \
                                                                    .replace("http://", "") \
                                                                    .replace("https://", "") \
                                                                    .replace("/", "")

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
                                                                            cursor.execute(sql, (
                                                                                activite.get('id'),
                                                                                capitale.get('id'),
                                                                                email))
                                                                            connection.commit()
                                                                            print(str(i_1) +
                                                                                  " The record is stored : " +
                                                                                  str(email))
                                                                            connection.close()
                                                                        except Exception as e:
                                                                            print(str(i_1) +
                                                                                  " The record already exists : " +
                                                                                  str(email) + " " + str(e))
                                                                            connection.close()
                                                                except Exception as e:
                                                                    print(str(e))
                                                            else:
                                                                print(str(i_1) + " no _blank")
                                                        except Exception as e:
                                                            print(str(e))
                                                    else:
                                                        print(str(i_1) + " no email business")
                                                except Exception as e:
                                                    print(str(e))
                                        else:
                                            print("sorry there is no results")
                                    except Exception as e:
                                        print(str(e))
                        except Exception as e:
                            print(str(e))
                    except Exception as e:
                        print(str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
