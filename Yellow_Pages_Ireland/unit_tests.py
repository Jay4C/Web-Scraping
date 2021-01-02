import time
from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesIreland(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://www.goldenpages.ie/attico-blackrock/"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'data-event-name': 'EmailClick'}) is not None:
            email = soup.find('a', {'data-event-name': 'EmailClick'}).get('href').lower().replace("mailto:", "").split("@")[1]
            print("email : info@" + email)

        else:
            print('no email business')

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        url_search = "https://www.goldenpages.ie/q/business/advanced/where/dublin/what/restaurant"
        html_search = requests.get(url_search)
        soup_search = BeautifulSoup(html_search.content, 'html.parser')
        number_of_pages = 0

        if soup_search.find('div', {'class': 'result_count'}) is not None:
            number_of_pages_with_coma = int(soup_search.find('div', {'class': 'result_count'}).text
                                            .replace("1 - 20 of ", "")
                                            .replace(",", "")
                                            .replace(" results", ""))/20

            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                number_of_pages += round(number_of_pages_with_coma) + 1
                print('number_of_pages : ' + str(number_of_pages))

            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                number_of_pages += round(number_of_pages_with_coma)
                print('number_of_pages : ' + str(number_of_pages))

        i_1 = 0

        try:
            for i in range(1, number_of_pages+1):
                url_of_one_page_of_results = url_search + "/" + str(i)
                time.sleep(2)
                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                if soup_of_one_page_of_results.find('div', {'class': 'listing_container'}) is not None:
                    for result_item in soup_of_one_page_of_results.find_all('div', {'class': 'listing_container'}):
                        i_1 += 1

                        url_result = "https://www.goldenpages.ie" + result_item.find('a', {'class': 'listing_base_link'})\
                            .get('href')

                        # Request the content of a page from the url
                        html_result = requests.get(url_result)

                        # Parse the content of html_doc
                        soup_result = BeautifulSoup(html_result.content, 'html.parser')

                        if soup_result.find('a', {'data-event-name': 'EmailClick'}) is not None:
                            email = "info@" + soup_result.find('a', {'data-event-name': 'EmailClick'})\
                                .get('href').lower()\
                                .replace("mailto:", "")\
                                .split("@")[1]
                            print(str(i_1) + " email : " + email)

                        else:
                            print('no email business')
                else:
                    print('sorry there is nothing')
        except:
            print("There is an error connection at url_page")

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            {'id': '1', 'url': '/what/Employment Agencies'}
            #{'id': '2', 'url': '/what/real estate'},
            #{'id': '3', 'url': '/what/recruiting'},
            #{'id': '4', 'url': '/what/software'},
            #{'id': '5', 'url': '/what/hotel'},
            #{'id': '6', 'url': '/what/landlord'},
            #{'id': '7', 'url': '/what/cleaning'},
            #{'id': '8', 'url': '/what/association'},
            #{'id': '9', 'url': '/what/restaurant'},
            #{'id': '10', 'url': '/what/financial'},
            #{'id': '11', 'url': '/what/building'},
            #{'id': '12', 'url': '/what/hairdresser'},
            #{'id': '13', 'url': '/what/florist'},
            #{'id': '14', 'url': '/what/locksmith'},
            #{'id': '15', 'url': '/what/bakery'},
            #{'id': '16', 'url': '/what/insurance'},
            #{'id': '17', 'url': '/what/pharmacy'},
            #{'id': '18', 'url': '/what/removal'},
            #{'id': '19', 'url': '/what/electricity'},
            #{'id': '20', 'url': '/what/plumbing'},
            #{'id': '21', 'url': '/what/security'},
            #{'id': '22', 'url': '/what/lawyer'},
            #{'id': '23', 'url': '/what/bank'},
            #{'id': '24', 'url': '/what/garage'},
            #{'id': '25', 'url': '/what/dentist'},
            #{'id': '26', 'url': '/what/doctor'},
            #{'id': '27', 'url': '/what/accounting'},
            #{'id': '28', 'url': '/what/supermarket'},
            #{'id': '29', 'url': '/what/notary'},
            #{'id': '30', 'url': '/what/jeweller'},
            #{'id': '31', 'url': '/what/tailor'},
            #{'id': '32', 'url': '/what/butcher'},
            #{'id': '33', 'url': '/what/bookseller'},
            #{'id': '34', 'url': '/what/architect'}
        ]

        capitales_du_monde = [
            #{'id': '138', 'nom': 'Dublin'}
            {'id': '139', 'nom': 'Carlow'},
            {'id': '140', 'nom': 'Dún Laoghaire'},
            {'id': '141', 'nom': 'Swords'},
            {'id': '142', 'nom': 'Tallaght'},
            {'id': '143', 'nom': 'Naas'},
            {'id': '144', 'nom': 'Kilkenny'},
            {'id': '145', 'nom': 'Port Laoise'},
            {'id': '146', 'nom': 'Longford'},
            {'id': '147', 'nom': 'Dundalk'},
            {'id': '148', 'nom': 'Navan'},
            {'id': '149', 'nom': 'Tullamore'},
            {'id': '150', 'nom': 'Mullingar'},
            {'id': '151', 'nom': 'Wexford'},
            {'id': '152', 'nom': 'Wicklow'},
            {'id': '153', 'nom': 'Ennis'},
            {'id': '154', 'nom': 'Cork'},
            {'id': '155', 'nom': 'Tralee'},
            {'id': '156', 'nom': 'Limerick'},
            {'id': '157', 'nom': 'Clonmel'},
            {'id': '158', 'nom': 'Nenagh'},
            {'id': '159', 'nom': 'Waterford'},
            {'id': '160', 'nom': 'Galway'},
            {'id': '161', 'nom': 'Carrick-on-Shannon'},
            {'id': '162', 'nom': 'Castlebar'},
            {'id': '163', 'nom': 'Roscommon'},
            {'id': '164', 'nom': 'Sligo'},
            {'id': '165', 'nom': 'Cavan'},
            {'id': '166', 'nom': 'Lifford'},
            {'id': '167', 'nom': 'Monaghan'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        url_search = "https://www.goldenpages.ie/q/business/advanced/where/" + capitale.get("nom") \
                                     + activite.get("url")

                        print("url_search : " + url_search)

                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')
                        number_of_pages = 0

                        if soup_search.find('div', {'class': 'result_count'}) is not None:
                            number_of_pages_with_coma = int(soup_search.find('div', {'class': 'result_count'}).text
                                                            .replace("1 - 20 of ", "")
                                                            .replace(",", "")
                                                            .replace(" results", "")) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                        i_1 = 0

                        try:
                            for i in range(1, number_of_pages + 1):
                                url_of_one_page_of_results = url_search + "/" + str(i)
                                time.sleep(2)
                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results)
                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results.find('div', {'class': 'listing_container'}) is not None:
                                    for result_item in soup_of_one_page_of_results\
                                            .find_all('div', {'class': 'listing_container'}):

                                        i_1 += 1

                                        url_result = "https://www.goldenpages.ie" + result_item\
                                            .find('a', {'class': 'listing_base_link'}).get('href')

                                        # Request the content of a page from the url
                                        html_result = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup_result = BeautifulSoup(html_result.content, 'html.parser')

                                        if soup_result.find('a', {'data-event-name': 'EmailClick'}) is not None:
                                            email = "info@" + soup_result.find('a', {'data-event-name': 'EmailClick'}) \
                                                .get('href').lower() \
                                                .replace("mailto:", "") \
                                                .split("@")[1]

                                            try:
                                                if validate_email(email, verify=True) != False:

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
                                                            print(str(i_1) + " The record is stored : " + str(email))
                                                            connection.close()
                                                        except:
                                                            print(str(i_1) + " The record already exists : "
                                                                  + str(email))
                                                            connection.close()
                                                else:
                                                    print(str(i_1) + " The email : " + email + " doesn't exist.")
                                            except:
                                                print(str(i_1) + " An error with the email : " + email)
                                        else:
                                            print(str(i_1) + ' no email business')
                                else:
                                    print('sorry there is nothing')
                        except:
                            print("There is an error connection at url_page")
                    except:
                        print("There is an error connection at url")
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
