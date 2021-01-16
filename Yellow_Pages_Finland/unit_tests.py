from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest


class UnitTestsDataMinerYellowPagesFinland(unittest.TestCase):
    def test_extract_email_from_one_result(self):
        print("test_extract_email_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.finder.fi/Hotelli/Original+Sokos+Hotel+Vaakuna+Pori/Pori/yhteystiedot/175394"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'listing-email'}) is not None:
            email = "info@" + soup.find('a', {'class': 'listing-email'}).get('href').split("@")[1]
            print("email type 1 : " + email)
        else:
            print("no email type 1")

    def test_extract_email_from_website_from_one_result(self):
        print("test_extract_email_from_website_from_one_result")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url = "https://www.finder.fi/Hotelli/Original+Sokos+Hotel+Vaakuna+Pori/Pori/yhteystiedot/175394"

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('a', {'class': 'listing-website-url'}) is not None:
            email = "info@" + soup.find('a', {'class': 'listing-website-url'}) \
                .get('href').replace("www.", "") \
                .replace("http://", "") \
                .replace("https://", "") \
                .split('/')[0] \
                .replace('/', '')
            print("email type 2 : " + email)
        else:
            print("no email type 2")

    def test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_one_page_of_results_for_one_activity_and_one_capital")

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        url_page_of_results = "https://www.finder.fi/search?what=hotel%20Helsinki&page=2"

        print(url_page_of_results)

        # Request the content of a page from the url
        html = requests.get(url_page_of_results, headers=headers)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'SearchResult'}) is not None:
            all_results = soup.find_all('div', {'class': 'SearchResult'})

            try:
                for result in all_results:
                    if result.find('a', {'class': 'SearchResult__ProfileLink'}) is not None:
                        url_result = "https://www.finder.fi" + result\
                            .find('a', {'class': 'SearchResult__ProfileLink'})\
                            .get('href')

                        # Request the content of a page from the url
                        html = requests.get(url_result, headers=headers)

                        # Parse the content of html_doc
                        soup = BeautifulSoup(html.content, 'html.parser')

                        if soup.find('a', {'class': 'listing-email'}) is not None:
                            email = "info@" + soup.find('a', {'class': 'listing-email'}).get('href').split("@")[1]
                            print("email type 1 : " + email)
                        else:
                            print("no email type 1")

                        if soup.find('a', {'class': 'listing-website-url'}) is not None:
                            email = "info@" + soup.find('a', {'class': 'listing-website-url'}) \
                                .get('href').replace("www.", "") \
                                .replace("http://", "") \
                                .replace("https://", "") \
                                .split('/')[0] \
                                .replace('/', '')
                            print("email type 2 : " + email)
                        else:
                            print("no email type 2")
                    else:
                        print("no a class SearchResult__ProfileLink")
            except Exception as e:
                print("error all_results : " + str(e))
        else:
            print("no div class SearchResult")

    def test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital(self):
        print("test_extract_each_email_from_all_pages_of_results_for_one_activity_and_one_capital")

        activity = "hotel"

        city = "Helsinki"

        url_search = "https://www.finder.fi/search?what=" + activity + " " + city

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        html_search = requests.get(url_search, headers=headers)

        soup_search = BeautifulSoup(html_search.content, 'html.parser')

        number_of_pages = 0

        try:
            if soup_search.find("a", {"class": "SearchResultList__MoreButton"}) is not None:
                number_of_pages_with_coma = int(soup_search.find("a", {"class": "SearchResultList__MoreButton"})
                                                .text
                                                .replace("Lisää tuloksia (25/", "")
                                                .replace(")", "")
                                                ) / 25

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))

                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))

                for i in range(1, number_of_pages + 1):
                    i_1 = 0

                    url_of_one_page_of_results = url_search + "&page=" + str(i)

                    print(url_of_one_page_of_results)

                    time.sleep(3)

                    html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content, 'html.parser')

                    if soup_of_one_page_of_results.find('div', {'class': 'SearchResult'}) is not None:
                        all_results = soup_of_one_page_of_results.find_all('div', {'class': 'SearchResult'})

                        try:
                            for result in all_results:
                                i_1 += 1

                                if result.find('a', {'class': 'SearchResult__ProfileLink'}) is not None:
                                    url_result = "https://www.finder.fi" + result \
                                        .find('a', {'class': 'SearchResult__ProfileLink'}) \
                                        .get('href')

                                    # Request the content of a page from the url
                                    html = requests.get(url_result, headers=headers)

                                    # Parse the content of html_doc
                                    soup = BeautifulSoup(html.content, 'html.parser')

                                    if soup.find('a', {'class': 'listing-email'}) is not None:
                                        email = "info@" + \
                                                soup.find('a', {'class': 'listing-email'}).get('href').split("@")[1]

                                        print(str(i_1) + " _ email type 1 : " + email)
                                    else:
                                        print(str(i_1) + " _ no email type 1")

                                    if soup.find('a', {'class': 'listing-website-url'}) is not None:
                                        email = "info@" + soup.find('a', {'class': 'listing-website-url'}) \
                                            .get('href').replace("www.", "") \
                                            .replace("http://", "") \
                                            .replace("https://", "") \
                                            .split('/')[0] \
                                            .replace('/', '')

                                        print(str(i_1) + " _ email type 2 : " + email)
                                    else:
                                        print(str(i_1) + " _ no email type 2")
                                else:
                                    print(str(i_1) + " _ no a class SearchResult__ProfileLink")
                        except Exception as e:
                            print("error all_results : " + str(e))
                    else:
                        print("no div class SearchResult")
            else:
                print("no pages at all")
        except Exception as e:
            print("error 2 : " + str(e))

    def test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals(self):
        print("test_extract_each_email_from_all_pages_of_results_for_all_activities_and_all_capitals")

        activites = [
            {'id': '1', 'url': 'job'},
            {'id': '2', 'url': 'kiinteä'},
            {'id': '3', 'url': 'rekrytointi'},
            {'id': '4', 'url': 'software'},
            {'id': '5', 'url': 'hotel'},
            {'id': '6', 'url': 'vuokranantaja'},
            {'id': '7', 'url': 'puhdistus'},
            {'id': '8', 'url': 'yhteiskunnassa'},
            {'id': '9', 'url': 'taloudellinen'},
            {'id': '10', 'url': 'ravintola'},
            {'id': '11', 'url': 'rakennus'},
            {'id': '12', 'url': 'kampaaja'},
            {'id': '13', 'url': 'kukkakauppias'},
            {'id': '14', 'url': 'lukkoseppä'},
            {'id': '15', 'url': 'leipomo'},
            {'id': '16', 'url': 'varmuus'},
            {'id': '17', 'url': 'apteekki'},
            {'id': '18', 'url': 'liikkua'},
            {'id': '19', 'url': 'sähköä'},
            {'id': '20', 'url': 'putkisto'},
            {'id': '21', 'url': 'turvallisuus'},
            {'id': '22', 'url': 'lakimies'},
            {'id': '23', 'url': 'pankki'},
            {'id': '24', 'url': 'autotalli'},
            {'id': '25', 'url': 'hammaslääkäri'},
            {'id': '26', 'url': 'lääkäri'},
            {'id': '27', 'url': 'kirjanpito'},
            {'id': '28', 'url': 'supermarket'},
            {'id': '29', 'url': 'notaari'},
            {'id': '30', 'url': 'helmi'},
            {'id': '31', 'url': 'ompelija'},
            {'id': '32', 'url': 'liha'},
            {'id': '33', 'url': 'kirjakauppa'},
            {'id': '34', 'url': 'arkkitehti'},
            {'id': '36', 'url': 'sementti'},
            {'id': '37', 'url': 'lämmitin'},
            {'id': '38', 'url': 'vene'},
            {'id': '39', 'url': 'kylmä'},
            {'id': '41', 'url': 'teräs'},
            {'id': '42', 'url': 'kemiallinen'},
            {'id': '43', 'url': 'kaasu'},
            {'id': '44', 'url': 'kulta'}
        ]

        capitales_du_monde = [
            {'id': '510', 'nom': 'Rovaniemi'},
            {'id': '511', 'nom': 'Oulu'},
            {'id': '512', 'nom': 'Kajaani'},
            {'id': '513', 'nom': 'Joensuu'},
            {'id': '514', 'nom': 'Kuopio'},
            {'id': '515', 'nom': 'Mikkeli'},
            {'id': '516', 'nom': 'Lappeenranta'},
            {'id': '517', 'nom': 'Jyväskylä'},
            {'id': '518', 'nom': 'Seinäjoki'},
            {'id': '519', 'nom': 'Vaasa'},
            {'id': '520', 'nom': 'Kokkola'},
            {'id': '521', 'nom': 'Tampere'},
            {'id': '522', 'nom': 'Pori'},
            {'id': '523', 'nom': 'Lahti'},
            {'id': '524', 'nom': 'Hämeenlinna'},
            {'id': '525', 'nom': 'Kouvola'},
            {'id': '526', 'nom': 'Kotka'},
            {'id': '527', 'nom': 'Helsinki'},
            {'id': '528', 'nom': 'Turku'},
            {'id': '529', 'nom': 'Porvoo'},
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    activity = activite.get('url')

                    city = capitale.get('nom')

                    url_search = "https://www.finder.fi/search?what=" + activity + " " + city

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
                    }

                    html_search = requests.get(url_search, headers=headers)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    number_of_pages = 0

                    try:
                        if soup_search.find("a", {"class": "SearchResultList__MoreButton"}) is not None:
                            number_of_pages_with_coma = int(
                                soup_search.find("a", {"class": "SearchResultList__MoreButton"})
                                .text
                                .replace("Lisää tuloksia (25/", "")
                                .replace(")", "")
                                ) / 25

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print('number_of_pages : ' + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print('number_of_pages : ' + str(number_of_pages))

                            for i in range(1, number_of_pages + 1):
                                i_1 = 0

                                url_of_one_page_of_results = url_search + "&page=" + str(i)

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                html_of_one_page_of_results = requests.get(url_of_one_page_of_results, headers=headers)

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                if soup_of_one_page_of_results.find('div', {'class': 'SearchResult'}) is not None:
                                    all_results = soup_of_one_page_of_results.find_all('div', {'class': 'SearchResult'})

                                    try:
                                        for result in all_results:
                                            i_1 += 1

                                            if result.find('a', {'class': 'SearchResult__ProfileLink'}) is not None:
                                                url_result = "https://www.finder.fi" + result \
                                                    .find('a', {'class': 'SearchResult__ProfileLink'}) \
                                                    .get('href')

                                                # Request the content of a page from the url
                                                html = requests.get(url_result, headers=headers)

                                                # Parse the content of html_doc
                                                soup = BeautifulSoup(html.content, 'html.parser')

                                                if soup.find('a', {'class': 'listing-email'}) is not None:
                                                    email = "info@" + \
                                                            soup.find('a', {'class': 'listing-email'}).get(
                                                                'href').split("@")[1]

                                                    print(str(i_1) + " _ email type 1 : " + email)

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
                                                                print(str(i_1)
                                                                      + " The record already exists : "
                                                                      + email
                                                                      + " " + str(e))
                                                                connection.close()
                                                    except Exception as e:
                                                        print(str(
                                                            i_1) + " An error with the email : " + email + " " + str(e))
                                                else:
                                                    print(str(i_1) + " _ no email type 1")

                                                if soup.find('a', {'class': 'listing-website-url'}) is not None:
                                                    email = "info@" + soup.find('a', {'class': 'listing-website-url'}) \
                                                        .get('href').replace("www.", "") \
                                                        .replace("http://", "") \
                                                        .replace("https://", "") \
                                                        .split('/')[0] \
                                                        .replace('/', '')

                                                    print(str(i_1) + " _ email type 2 : " + email)

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
                                                                print(str(i_1)
                                                                      + " The record already exists : "
                                                                      + email
                                                                      + " " + str(e))
                                                                connection.close()
                                                    except Exception as e:
                                                        print(str(
                                                            i_1) + " An error with the email : " + email + " " + str(e))
                                                else:
                                                    print(str(i_1) + " _ no email type 2")
                                            else:
                                                print(str(i_1) + " _ no a class SearchResult__ProfileLink")
                                    except Exception as e:
                                        print("error all_results : " + str(e))
                                else:
                                    print("no div class SearchResult")
                        else:
                            print("no pages at all")
                    except Exception as e:
                        print("error 2 : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
