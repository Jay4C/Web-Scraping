from bs4 import BeautifulSoup
import requests
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesRussia(unittest.TestCase):
    def test_extract_one_email(self):
        url = "https://msk.yp.ru/detail/id/mamaison_all_suites_spa_hotel_pokrovka_1152089/"

        # Request the content of a page from the url
        html = requests.get(url)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, "html.parser")

        if soup.find("a", {"data-statclick-action": "is_web"}) is not None:
            all_is_web = soup.find_all("a", {"data-statclick-action": "is_web"})

            for is_web in all_is_web:
                email = "info@" + is_web.get("data-statclick-url")\
                    .replace("www.", "")\
                    .replace("http://", "")\
                    .replace("https://", "")\

                try:
                    if validate_email(email, verify=True) != False:
                        print("The email : " + email + " does exist.")
                    else:
                        print("The email : " + email + " doesn't exist.")
                except:
                    print("An error with the email : " + email)
        else:
            print("no email business")

    def test_extract_emails_from_all_page_of_results_for_one_activity_and_capital(self):
        try:
            activity = "hotel"
            city = "https://msk.yp.ru/search/text/"
            url_search = city + activity
            html_search = requests.get(url_search)
            soup_search = BeautifulSoup(html_search.content, "html.parser")

            number_of_pages = 0

            try:
                if soup_search \
                        .select_one("#utm") \
                        .find("div", {"class": "row companies-container"}) is not None:
                    try:
                        if soup_search \
                                .select_one("#utm") \
                                .find("div", {"class": "row companies-container"}) \
                                .find("div", {"class": "mdl-cell mdl-cell--12-col"}) is not None:

                            number_of_pages_with_coma = int(soup_search
                                                            .select_one("#utm")
                                                            .find("div", {"class": "row companies-container"})
                                                            .find("div", {"class": "mdl-cell mdl-cell--12-col"})
                                                            .text
                                                            .replace("\t", "")
                                                            .replace("\n", "")
                                                            .replace(" ", "")
                                                            .replace("Нашлось", "")
                                                            .replace("компании", "")
                                                            ) / 20

                            if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                number_of_pages += round(number_of_pages_with_coma) + 1
                                print("number_of_pages : " + str(number_of_pages))

                            elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                number_of_pages += round(number_of_pages_with_coma)
                                print("number_of_pages : " + str(number_of_pages))
                        else:
                            print("no div mdl-cell mdl-cell--12-col")
                    except Exception as e:
                        print("error mdl-cell mdl-cell--12-col : " + str(e))
                else:
                    print("no div row companies-container")
            except Exception as e:
                print("error row companies-container : " + str(e))

            i_1 = 0

            try:
                for i in range(48, number_of_pages+1):
                    url_one_page_of_results = city + activity + "/page/" + str(i) + "/"

                    print(url_one_page_of_results)

                    html_search = requests.get(url_one_page_of_results)
                    soup_one_page_of_results = BeautifulSoup(html_search.content, "html.parser")

                    if soup_one_page_of_results\
                        .select_one("#companies") is not None:
                        if soup_one_page_of_results\
                            .select_one("#companies")\
                            .find("div", {"class": "row"}) is not None:

                            all_row = soup_one_page_of_results.select_one("#companies").find_all("div", {"class": "row"})

                            for j in range(0, len(all_row)):
                                i_1 += 1

                                if all_row[j].find("div", {"class": "company__head"}) is not None:
                                    if all_row[j]\
                                        .find("div", {"class": "company__head"})\
                                        .find("a", {"class": "testtjlw"}) is not None:
                                        url_result = "https://msk.yp.ru" + all_row[j]\
                                            .find("div", {"class": "company__head"})\
                                            .find("a", {"class": "testtjlw"})\
                                            .get("href")

                                        print(url_result)

                                        # Request the content of a page from the url
                                        html = requests.get(url_result)

                                        # Parse the content of html_doc
                                        soup = BeautifulSoup(html.content, "html.parser")

                                        if soup.find("a", {"data-statclick-action": "is_web"}) is not None:
                                            all_is_web = soup.find_all("a", {"data-statclick-action": "is_web"})

                                            for is_web in all_is_web:
                                                email = "info@" + is_web.get("data-statclick-url") \
                                                    .replace("www.", "") \
                                                    .replace("http://", "") \
                                                    .replace("https://", "")\
                                                    .split("/")[0]

                                                try:
                                                    if validate_email(email, verify=True) != False:
                                                        print(str(i_1) + " The email : " + email + " does exist.")
                                                    else:
                                                        print(str(i_1) + " The email : " + email + " doesn't exist.")
                                                except:
                                                    print(str(i_1) + " An error with the email : " + email)
                                        else:
                                            print(str(i_1) + " no email business")
                                    else:
                                        print(str(i_1) + " no a testtjlw")
                                else:
                                    print(str(i_1) + " no div company__head")
                        else:
                            print("no div row")
                    else:
                        print("no id companies")
            except Exception as e:
                print("error page : " + str(e))
        except Exception as e:
            print("url_search : " + str(e))

    def test_extract_emails_from_all_page_of_results_for_all_activities_and_capitals(self):
        activites = [
            # {'id': '1', 'url': 'временное+агентство'},
            # {'id': '2', 'url': 'агентство+недвижимости'},
            # {'id': '3', 'url': 'кадровое+агентство'},
            # {'id': '4', 'url': 'software'},
            # {'id': '5', 'url': 'hotel'},
            # {'id': '6', 'url': 'социальный+арендодатель'},
            # {'id': '7', 'url': 'клининговая+компания'},
            # {'id': '8', 'url': 'ассоциация'},
            # {'id': '9', 'url': 'финансовое+учреждение'},
            # {'id': '10', 'url': 'ресторан'},
            # {'id': '11', 'url': 'строительная+компания'},
            # {'id': '12', 'url': 'парикмахер'},
            # {'id': '13', 'url': 'флорист'},
            # {'id': '14', 'url': 'слесарь'},
            # {'id': '15', 'url': 'пекарня'},
            # {'id': '16', 'url': 'страхование'},
            # {'id': '17', 'url': 'аптека'},
            # {'id': '18', 'url': 'транспортная+компания'},
            # {'id': '19', 'url': 'электричество'},
            # {'id': '20', 'url': 'водопровод'},
            # {'id': '21', 'url': 'охранная+компания'},
            # {'id': '22', 'url': 'адвокат'},
            # {'id': '23', 'url': 'банк'},
            # {'id': '24', 'url': 'гараж'},
            # {'id': '25', 'url': 'дантист'},
            # {'id': '26', 'url': 'врач'},
            # {'id': '27', 'url': 'учет'},
            # {'id': '28', 'url': 'супермаркет'},
            # {'id': '29', 'url': 'нотариус'},
            # {'id': '30', 'url': 'ювелир'},
            # {'id': '31', 'url': 'модельер'},
            # {'id': '32', 'url': 'мясник'},
            # {'id': '33', 'url': 'книжный+магазин'},
            # {'id': '34', 'url': 'архитектор'}
            {'id': '36', 'url': 'цемента'},
            {'id': '37', 'url': 'отопление'},
            {'id': '38', 'url': 'лодке'},
            {'id': '39', 'url': 'холодной'},
            {'id': '41', 'url': 'стали'},
            {'id': '42', 'url': 'химических'},
            {'id': '43', 'url': 'газа'},
            {'id': '44', 'url': 'покупка+золота'}
        ]

        capitales_du_monde = [
            {'id': '453', 'nom': 'https://msk.yp.ru/search/text/'}, # Moscow
            {'id': '454', 'nom': 'https://www.yp.ru/search/text/'}, # St Petersburg
            {'id': '455', 'nom': 'https://abakan.yp.ru/search/text/'}, #
            {'id': '456', 'nom': 'https://yarovoe.yp.ru/search/text/'},
            {'id': '457', 'nom': 'https://alatyr.yp.ru/search/text/'},
            {'id': '458', 'nom': 'https://agidel.yp.ru/search/text/'},
            {'id': '459', 'nom': 'https://alekseevka.yp.ru/search/text/'},
            {'id': '460', 'nom': 'https://abinsk.yp.ru/search/text/'},
            {'id': '461', 'nom': 'https://abakan.yp.ru/search/text/'},
            {'id': '462', 'nom': 'https://yasnyi.yp.ru/search/text/'},
            {'id': '463', 'nom': 'https://azov.yp.ru/search/text/'},
            {'id': '464', 'nom': 'https://aldan.yp.ru/search/text/'},
            {'id': '465', 'nom': 'https://alagir.yp.ru/search/text/'},
            {'id': '466', 'nom': 'https://yartsevo.yp.ru/search/text/'},
            {'id': '467', 'nom': 'https://alapaevsk.yp.ru/search/text/'},
            {'id': '468', 'nom': 'https://agryz.yp.ru/search/text/'},
            {'id': '469', 'nom': 'https://yasnogorsk.yp.ru/search/text/'},
            {'id': '470', 'nom': 'https://ak-dovurak.yp.ru/search/text/'},
            {'id': '471', 'nom': 'https://yaroslavl.yp.ru/search/text/'},
            {'id': '472', 'nom': 'https://aleksandrovsk.yp.ru/search/text/'}
        ]

        try:
            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")
                        url_search = city + activity
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, "html.parser")

                        number_of_pages = 0

                        try:
                            if soup_search \
                                    .select_one("#utm") \
                                    .find("div", {"class": "row companies-container"}) is not None:
                                try:
                                    if soup_search \
                                            .select_one("#utm") \
                                            .find("div", {"class": "row companies-container"}) \
                                            .find("div", {"class": "mdl-cell mdl-cell--12-col"}) is not None:

                                        number_of_pages_with_coma = int(soup_search
                                                                        .select_one("#utm")
                                                                        .find("div",
                                                                              {"class": "row companies-container"})
                                                                        .find("div",
                                                                              {"class": "mdl-cell mdl-cell--12-col"})
                                                                        .text
                                                                        .replace("\t", "")
                                                                        .replace("\n", "")
                                                                        .replace(" ", "")
                                                                        .replace("Нашлось", "")
                                                                        .replace("компании", "")
                                                                        .replace("компаний", "")
                                                                        ) / 20

                                        if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                            number_of_pages += round(number_of_pages_with_coma) + 1
                                            print("number_of_pages : " + str(number_of_pages))

                                        elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                            number_of_pages += round(number_of_pages_with_coma)
                                            print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no div mdl-cell mdl-cell--12-col")
                                except Exception as e:
                                    print("error mdl-cell mdl-cell--12-col : " + str(e))
                            else:
                                print("no div row companies-container")
                        except Exception as e:
                            print("error row companies-container : " + str(e))

                        i_1 = 0

                        try:
                            for i in range(1, number_of_pages + 1):
                                url_one_page_of_results = city + activity + "/page/" + str(i) + "/"

                                print(url_one_page_of_results)

                                html_search = requests.get(url_one_page_of_results)
                                soup_one_page_of_results = BeautifulSoup(html_search.content, "html.parser")

                                if soup_one_page_of_results \
                                        .select_one("#companies") is not None:
                                    if soup_one_page_of_results \
                                            .select_one("#companies") \
                                            .find("div", {"class": "row"}) is not None:

                                        all_row = soup_one_page_of_results.select_one("#companies").find_all("div", {
                                            "class": "row"})

                                        for j in range(0, len(all_row)):
                                            i_1 += 1

                                            if all_row[j].find("div", {"class": "company__head"}) is not None:
                                                if all_row[j] \
                                                        .find("div", {"class": "company__head"}) \
                                                        .find("a", {"class": "testtjlw"}) is not None:
                                                    url_result = "https://msk.yp.ru" + all_row[j] \
                                                        .find("div", {"class": "company__head"}) \
                                                        .find("a", {"class": "testtjlw"}) \
                                                        .get("href")

                                                    print(url_result)

                                                    # Request the content of a page from the url
                                                    html = requests.get(url_result)

                                                    # Parse the content of html_doc
                                                    soup = BeautifulSoup(html.content, "html.parser")

                                                    if soup.find("a", {"data-statclick-action": "is_web"}) is not None:
                                                        all_is_web = soup.find_all("a",
                                                                                   {"data-statclick-action": "is_web"})

                                                        for is_web in all_is_web:
                                                            email = "info@" + is_web.get("data-statclick-url") \
                                                                .replace("www.", "") \
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
                                                                        print(str(i_1) + " The record is stored : "
                                                                              + str(email))
                                                                        connection.close()
                                                                    except Exception as e:
                                                                        print(str(i_1)
                                                                              + " The record already exists : "
                                                                              + str(email) + " "
                                                                              + str(e))
                                                                        connection.close()
                                                            except Exception as e:
                                                                print(str(i_1)
                                                                      + " An error with the email : "
                                                                      + email + " "
                                                                      + str(e)
                                                                      )
                                                    else:
                                                        print(str(i_1) + " no email business")
                                                else:
                                                    print(str(i_1) + " no a testtjlw")
                                            else:
                                                print(str(i_1) + " no div company__head")
                                    else:
                                        print("no div row")
                                else:
                                    print("no id companies")
                        except Exception as e:
                            print("error " + str(e))
                    except Exception as e:
                        print("url_search : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
