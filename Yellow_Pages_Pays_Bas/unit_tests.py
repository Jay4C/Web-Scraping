import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesPaysBas(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.telefoonboek.nl/bedrijven/t2041321/amsterdam/strego-juwelier/"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-event-category': 'Website'}) is not None:
            email = "info@" + soup.find('a', {'data-event-category': 'Website'})\
                .get("href")\
                .replace("http://www.", "")\
                .replace("https://www.", "")

            try:
                if validate_email(email, verify=True) != False:
                    print("email : " + email + " does exist")
                else:
                    print("The email : " + email + " doesn't exist.")
            except:
                print("An error with the email : " + email)
        else:
            print("no email business")

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        activity = "juwelier"
        city = "amsterdam"
        url_search = "https://www.telefoonboek.nl/zoeken/" + activity + "/" + city + "/"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.select_one("#content")\
                .find("article",  {"class": "intro"})\
                .find("div",  {"class": "heading"}) is not None:

            number_of_pages_with_coma = int(
                soup_search.select_one("#content")
                .find("article", {"class": "intro"})
                .find("div", {"class": "heading"})
                .find("h3")
                .text
                .lower()
                .replace("\t", " ")
                .replace("\n", " ")
                .replace(" ", "")
                .replace("resultaten1-20getoondvan", "")
                .replace(activity + "in" + city, "")
            ) / 20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        for i in range(1, number_of_pages + 1):
            url_of_one_page_of_results = url_search + "pagina" + str(i) + "/"
            print(url_of_one_page_of_results)
            time.sleep(2)
            html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
            soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

            if soup_of_one_page_of_results\
                    .select_one("#content") is not None:
                for result_item in soup_of_one_page_of_results\
                        .select_one("#content")\
                        .find_all("ul", {"data-marker-type": "company"}):
                    i_1 += 1

                    url_result = "https://www.telefoonboek.nl" + result_item.get("data-url")

                    time.sleep(2)

                    # Request the content of a page from the url
                    html = requests.get(url_result)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(html.content, 'html.parser')

                    if soup.find('a', {'data-event-category': 'Website'}) is not None:
                        email = "info@" + soup \
                            .find('a', {'data-event-category': 'Website'}) \
                            .get("href") \
                            .replace("http://www.", "") \
                            .replace("https://www.", "") \
                            .replace("http://", "") \
                            .replace("https://", "") \
                            .split("/")[0]

                        try:
                            if validate_email(email, verify=True) != False:
                                print(str(i_1) + " - The email : " + email + " does exist")
                            else:
                                print(str(i_1) + " - The email : " + email + " doesn't exist.")
                        except:
                            print(str(i_1) + " - An error with the email : " + email)
                    else:
                        print(str(i_1) + " - No email business")
            else:
                print("there is no results")

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'baan'}
            # {'id': '2', 'url': 'makelaar'},
            # {'id': '3', 'url': 'recruiter'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'verhuurder'},
            # {'id': '7', 'url': 'schoonmaken'},
            # {'id': '8', 'url': 'vereniging'},
            # {'id': '9', 'url': 'financieel'},
            # {'id': '10', 'url': 'restaurant'},
            # {'id': '11', 'url': 'gebouw'},
            # {'id': '12', 'url': 'kapper'},
            # {'id': '13', 'url': 'bloemist'},
            # {'id': '14', 'url': 'slotenmaker'},
            # {'id': '15', 'url': 'bakkerij'},
            # {'id': '16', 'url': 'verzekering'},
            # {'id': '17', 'url': 'apotheek'},
            # {'id': '18', 'url': 'verhuizer'},
            # {'id': '19', 'url': 'elektriciteit'},
            # {'id': '20', 'url': 'sanitair'},
            # {'id': '21', 'url': 'beveiliging'},
            # {'id': '22', 'url': 'advocaat'},
            # {'id': '23', 'url': 'bank'},
            # {'id': '24', 'url': 'garage'},
            # {'id': '25', 'url': 'tandarts'},
            # {'id': '26', 'url': 'dokter'},
            # {'id': '27', 'url': 'accounting'},
            # {'id': '28', 'url': 'supermarkt'},
            # {'id': '29', 'url': 'notaris'},
            # {'id': '30', 'url': 'juwelier'},
            # {'id': '31', 'url': 'modeontwerper'},
            # {'id': '32', 'url': 'slager'},
            # {'id': '33', 'url': 'boekhandel'},
            # {'id': '34', 'url': 'architect'},
            {'id': '36', 'url': 'cementfabriek'},  # cimenterie
            {'id': '37', 'url': 'kachel'},  # chauffage
            {'id': '38', 'url': 'boot'},  # naval
            {'id': '39', 'url': 'airco'},  # froid
            {'id': '41', 'url': 'staalindustrie'},  # sidérurgie
            {'id': '42', 'url': 'chemisch'},  # industrie chimique
            {'id': '43', 'url': 'gas'},  # gaz
            {'id': '44', 'url': 'goud-kopen'}  # achat or
        ]

        capitales_du_monde = [
            # {'id': '259', 'nom': 'assen'} #Assen
            # {'id': '260', 'nom': 'emmen'}, #Emmen
            # {'id': '261', 'nom': 'lelystad'}, #Lelystad
            # {'id': '262', 'nom': 'almere'}, #Almere
            # {'id': '263', 'nom': 'leeuwarden'}, #Leeuwarden
            # {'id': '264', 'nom': 'arnhem'}, #Arnhem
            {'id': '265', 'nom': 'nijmegen'}, #Nijmegen
            # {'id': '266', 'nom': 'groningen'}, #Groningen
            # {'id': '267', 'nom': 'maastricht'}, #Maastricht
            # {'id': '268', 'nom': 's-hertogenbosch'}, #S hertogenbosch
            # {'id': '269', 'nom': 'eindhoven'}, #Eindhoven
            # {'id': '270', 'nom': 'haarlem'}, #Haarlem
            # {'id': '271', 'nom': 'amsterdam'}, #Amsterdam
            # {'id': '272', 'nom': 'zwolle'}, #Zwolle
            # {'id': '273', 'nom': 'enschede'}, #Enschede
            # {'id': '274', 'nom': 'the-hague'}, #The hague
            # {'id': '275', 'nom': 'utrecht'}, #Utrecht
            # {'id': '276', 'nom': 'middelburg'}, #Middelburg
            # {'id': '277', 'nom': 'terneuzen'}, #Terneuzen
            # {'id': '278', 'nom': 'rotterdam'} #Rotterdam
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")
                        url_search = "https://www.telefoonboek.nl/zoeken/" + activity + "/" + city + "/"
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.select_one("#content") \
                                .find("article", {"class": "intro"}) \
                                .find("div", {"class": "heading"}) is not None:

                            number_of_pages_with_coma = int(
                                soup_search.select_one("#content")
                                .find("article", {"class": "intro"})
                                .find("div", {"class": "heading"})
                                .find("h3")
                                .text
                                .lower()
                                .replace("\t", " ")
                                .replace("\n", " ")
                                .replace(" ", "")
                                .replace("resultaten", "")
                                .replace(activity + "in" + city, "")
                                .split("getoondvan")[1]
                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                            i_1 = 0

                            for i in range(1, number_of_pages + 1):
                                url_of_one_page_of_results = url_search + "pagina" + str(i) + "/"
                                print(url_of_one_page_of_results)
                                time.sleep(2)
                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results \
                                        .select_one("#content") is not None:
                                    for result_item in soup_of_one_page_of_results \
                                            .select_one("#content") \
                                            .find_all("ul", {"data-marker-type": "company"}):
                                        i_1 += 1

                                        url_result = "https://www.telefoonboek.nl" + result_item.get("data-url")

                                        time.sleep(2)

                                        # Request the content of a page from the url
                                        html = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, 'html.parser')

                                        if soup.find('a', {'data-event-category': 'Website'}) is not None:
                                            email = "info@" + soup \
                                                .find('a', {'data-event-category': 'Website'}) \
                                                .get("href") \
                                                .replace("http://www.", "") \
                                                .replace("https://www.", "") \
                                                .replace("http://", "") \
                                                .replace("https://", "") \
                                                .split("/")[0]

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
                                                        print(str(i_1) + " The record is stored : " + email)
                                                        connection.close()
                                                    except Exception as e:
                                                        print(str(e) + " - " + str(i_1) + " The record already exists : " + email)
                                                        connection.close()
                                            except Exception as e:
                                                print(str(e) + "- " + str(i_1) + " - An error with the email : " + email)
                                        else:
                                            print(str(i_1) + " - No email business")
                                else:
                                    print("there is no results")
                        else:
                            print("no content")
                    except Exception as e:
                        print(str(e) + " - url search : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
