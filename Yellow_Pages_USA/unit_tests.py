from bs4 import BeautifulSoup
import requests
import time
import pymysql.cursors
import unittest
from validate_email import validate_email


class UnitTestsDataMinerYellowPagesUsa(unittest.TestCase):
    def test_web_scraper_email_usa(self):
        activites = [
            {'id': '1',
                'url': 'https://www.yellowpages.com/search?search_terms=Temporary+Employment+Agencies&geo_location_terms='},
            {'id': '2', 'url': 'https://www.yellowpages.com/search?search_terms=real+estate&geo_location_terms='},
            {'id': '3', 'url': 'https://www.yellowpages.com/search?search_terms=Recruiter&geo_location_terms='},
            {'id': '4', 'url': 'https://www.yellowpages.com/search?search_terms=software&geo_location_terms='},
            {'id': '5', 'url': 'https://www.yellowpages.com/search?search_terms=hotel&geo_location_terms='},
            {'id': '6',
                'url': 'https://www.yellowpages.com/search?search_terms=social+landlord&geo_location_terms='},
            {'id': '7', 'url': 'https://www.yellowpages.com/search?search_terms=cleaning&geo_location_terms='},
            {'id': '8', 'url': 'https://www.yellowpages.com/search?search_terms=Charities&geo_location_terms='},
            {'id': '9', 'url': 'https://www.yellowpages.com/search?search_terms=financial&geo_location_terms='},
            {'id': '10', 'url': 'https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms='},
            {'id': '11', 'url': 'https://www.yellowpages.com/search?search_terms=building&geo_location_terms='},
            {'id': '12', 'url': 'https://www.yellowpages.com/search?search_terms=hairdresser&geo_location_terms='},
            {'id': '13', 'url': 'https://www.yellowpages.com/search?search_terms=florist&geo_location_terms='},
            {'id': '14', 'url': 'https://www.yellowpages.com/search?search_terms=locksmith&geo_location_terms='},
            {'id': '15', 'url': 'https://www.yellowpages.com/search?search_terms=bakery&geo_location_terms='},
            {'id': '16', 'url': 'https://www.yellowpages.com/search?search_terms=insurance&geo_location_terms='},
            {'id': '17', 'url': 'https://www.yellowpages.com/search?search_terms=Pharmacies&geo_location_terms='},
            {'id': '18', 'url': 'https://www.yellowpages.com/search?search_terms=movers&geo_location_terms='},
            {'id': '19', 'url': 'https://www.yellowpages.com/search?search_terms=electricity&geo_location_terms='},
            {'id': '20', 'url': 'https://www.yellowpages.com/search?search_terms=plumbing&geo_location_terms='},
            {'id': '21', 'url': 'https://www.yellowpages.com/search?search_terms=security&geo_location_terms='},
            {'id': '22', 'url': 'https://www.yellowpages.com/search?search_terms=attorney&geo_location_terms='},
            {'id': '23', 'url': 'https://www.yellowpages.com/search?search_terms=bank&geo_location_terms='},
            {'id': '24', 'url': 'https://www.yellowpages.com/search?search_terms=mechanic&geo_location_terms='},
            {'id': '25', 'url': 'https://www.yellowpages.com/search?search_terms=dentist&geo_location_terms='},
            {'id': '26', 'url': 'https://www.yellowpages.com/search?search_terms=doctor&geo_location_terms='},
            {'id': '27', 'url': 'https://www.yellowpages.com/search?search_terms=accountant&geo_location_terms='},
            {'id': '28',
                'url': 'https://www.yellowpages.com/search?search_terms=Grocery+Stores&geo_location_terms='},
            {'id': '29', 'url': 'https://www.yellowpages.com/search?search_terms=notary&geo_location_terms='},
            {'id': '30', 'url': 'https://www.yellowpages.com/search?search_terms=jewellery&geo_location_terms='},
            {'id': '31', 'url': 'https://www.yellowpages.com/search?search_terms=tailors&geo_location_terms='},
            {'id': '32', 'url': 'https://www.yellowpages.com/search?search_terms=butcher&geo_location_terms='},
            {'id': '33', 'url': 'https://www.yellowpages.com/search?search_terms=library&geo_location_terms='},
            {'id': '34', 'url': 'https://www.yellowpages.com/search?search_terms=Architects&geo_location_terms='}
        ]

        capitales_du_monde = [
            {'id': '2', 'nom': 'New+York%2C+NY'},
            # {'id': '4', 'nom': 'Chicago%2C+IL'},
            # {'id': '5', 'nom': 'Atlanta%2C+GA'},
            # {'id': '6', 'nom': 'Houston%2C+TX'},
            # {'id': '7', 'nom': 'Los+Angeles%2C+CA'},
            # {'id': '9', 'nom': 'Albany%2C+NY'},
            # {'id': '36', 'nom': 'Montgomery%2C+AL'},
            # {'id': '37', 'nom': 'Birmingham%2C+AL'},
            # {'id': '38', 'nom': 'Juneau%2C+AK'},
            # {'id': '39', 'nom': 'Anchorage%2C+AK'},
            # {'id': '40', 'nom': 'Phoenix%2C+AZ'},
            # {'id': '41', 'nom': 'Little+Rock%2C+AR'},
            # {'id': '42', 'nom': 'Sacramento%2C+CA'},
            # {'id': '43', 'nom': 'Denver%2C+CO'},
            # {'id': '44', 'nom': 'Hartford%2C+CT'},
            # {'id': '45', 'nom': 'Bridgeport%2C+CT'},
            # {'id': '46', 'nom': 'Dover%2C+DE'},
            # {'id': '47', 'nom': 'Wilmington%2C+DE'},
            # {'id': '48', 'nom': 'Tallahassee%2C+FL'},
            # {'id': '49', 'nom': 'Jacksonville%2C+FL'},
            # {'id': '50', 'nom': 'Honolulu%2C+HI'},
            # {'id': '51', 'nom': 'Boise%2C+ID'},
            # {'id': '52', 'nom': 'Springfield%2C+IL'},
            # {'id': '53', 'nom': 'Indianapolis%2C+IN'},
            # {'id': '54', 'nom': 'Des+Moines%2C+IA'},
            # {'id': '55', 'nom': 'Topeka%2C+KS'},
            # {'id': '56', 'nom': 'Wichita%2C+KS'},
            # {'id': '57', 'nom': 'Frankfort%2C+KY'},
            # {'id': '58', 'nom': 'Louisville%2C+KY'},
            # {'id': '59', 'nom': 'Baton+Rouge%2C+LA'},
            # {'id': '60', 'nom': 'New+Orleans%2C+LA'},
            # {'id': '61', 'nom': 'Augusta%2C+ME'},
            # {'id': '62', 'nom': 'Portland%2C+ME'},
            # {'id': '63', 'nom': 'Annapolis%2C+MD'},
            # {'id': '64', 'nom': 'Baltimore%2C+MD'},
            # {'id': '65', 'nom': 'Boston%2C+MA'},
            # {'id': '66', 'nom': 'Lansing%2C+MI'},
            # {'id': '67', 'nom': 'Detroit%2C+MI'},
            # {'id': '68', 'nom': 'Saint+Paul%2C+MN'},
            # {'id': '69', 'nom': 'Minneapolis%2C+MN'},
            # {'id': '70', 'nom': 'Jackson%2C+MS'},
            # {'id': '71', 'nom': 'Jefferson+City%2C+MO'},
            # {'id': '72', 'nom': 'Kansas+City%2C+MO'},
            # {'id': '73', 'nom': 'Helena%2C+MT'},
            # {'id': '74', 'nom': 'Billings%2C+MT'},
            # {'id': '75', 'nom': 'Lincoln%2C+NE'},
            # {'id': '76', 'nom': 'Omaha%2C+NE'},
            # {'id': '77', 'nom': 'Carson+City%2C+NV'},
            # {'id': '78', 'nom': 'Las+Vegas%2C+NV'},
            # {'id': '79', 'nom': 'Concord%2C+NH'},
            # {'id': '80', 'nom': 'Manchester%2C+NH'}
            # {'id': '81', 'nom': 'Trenton%2C+NJ'},
            # {'id': '82', 'nom': 'Newark%2C+NJ'},
            # {'id': '83', 'nom': 'Santa+Fe%2C+NM'},
            # {'id': '84', 'nom': 'Albuquerque%2C+NM'},
            # {'id': '85', 'nom': 'Raleigh%2C+NC'},
            # {'id': '86', 'nom': 'Charlotte%2C+NC'},
            # {'id': '87', 'nom': 'Bismarck%2C+ND'},
            # {'id': '88', 'nom': 'Columbus%2C+OH'},
            # {'id': '89', 'nom': 'Oklahoma+City%2C+OK'},
            # {'id': '90', 'nom': 'Salem%2C+OR'},
            # {'id': '91', 'nom': 'Portland%2C+OR'},
            # {'id': '92', 'nom': 'Harrisburg%2C+PA'},
            # {'id': '93', 'nom': 'Philadelphia%2C+PA'},
            # {'id': '94', 'nom': 'Providence%2C+RI'},
            # {'id': '95', 'nom': 'Columbia%2C+SC'},
            # {'id': '96', 'nom': 'Pierre%2C+SD'},
            # {'id': '97', 'nom': 'Sioux+Falls%2C+SD'},
            # {'id': '98', 'nom': 'Nashville%2C+TN'},
            # {'id': '99', 'nom': 'Memphis%2C+TN'},
            # {'id': '100', 'nom': 'Austin%2C+TX'},
            # {'id': '101', 'nom': 'Salt+Lake+City%2C+UT'},
            # {'id': '102', 'nom': 'Montpelier%2C+VT'},
            # {'id': '103', 'nom': 'Burlington%2C+VT'},
            # {'id': '104', 'nom': 'Richmond%2C+VA'},
            # {'id': '105', 'nom': 'Olympia%2C+WA'},
            # {'id': '106', 'nom': 'Seattle%2C+WA'},
            # {'id': '107', 'nom': 'Charleston%2C+WV'},
            # {'id': '108', 'nom': 'Madison%2C+WI'},
            # {'id': '109', 'nom': 'Milwaukee%2C+WI'},
            # {'id': '110', 'nom': 'Cheyenne%2C+WY'}
        ]

        try:
            for capitale_du_monde in capitales_du_monde:
                for activite in activites:
                    i_1 = 0

                    i = 1

                    var = 1

                    while var == 1 and i < 102:
                        try:
                            url = activite.get('url') + capitale_du_monde.get('nom') + "&page=" + str(i)

                            # Request the content of a page from the url
                            html = requests.get(url)

                            time.sleep(3)

                            # Parse the content of html_doc
                            soup = BeautifulSoup(html.content, 'html.parser')

                            print(url)

                            if soup.find("a", {"class", "business-name"}) is None:
                                print('sorry there is nothing')
                                break
                            else:
                                try:
                                    for link in soup.find_all("a", {"class": "business-name"}):
                                        i_1 += 1

                                        # Request the content of a page from the url
                                        url_page = "https://www.yellowpages.com" + link.get('href')

                                        html_doc = requests.get(url_page)

                                        time.sleep(3)

                                        # Parse the content of html_doc
                                        soup_link = BeautifulSoup(html_doc.content, 'html.parser')

                                        if soup_link.find("a", {"class": "email-business"}) is not None:
                                            email_business = soup_link.select(".email-business")[0].get('href')[7:]

                                            suffixes = [
                                                "info@"
                                            ]

                                            for suffix in suffixes:
                                                email = str(suffix + email_business.split("@")[1])

                                                try:
                                                    is_valid = validate_email(
                                                        email_address=email,
                                                        check_regex=True,
                                                        check_mx=True,
                                                        from_address='',
                                                        helo_host='',
                                                        smtp_timeout=10,
                                                        dns_timeout=10,
                                                        use_blacklist=True
                                                    )

                                                    if is_valid:
                                                        try:
                                                            # Connect to the database
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
                                                                        capitale_du_monde.get('id'),
                                                                        email))
                                                                    connection.commit()
                                                                    print(str(i_1) + " The record is stored : "
                                                                            + str(email))
                                                                    connection.close()
                                                                except Exception as e:
                                                                    print(str(i_1) + " The record already exists : "
                                                                            + str(email) + " " + str(e))
                                                                    connection.close()
                                                        except Exception as e:
                                                            print("Problem connection MySQL : " + str(e))
                                                    else:
                                                        print(
                                                            str(i_1) + " The email : " + email + " doesn't exist.")
                                                except Exception as e:
                                                    print(str(
                                                        i_1) + " An error with the email : " + email + " " + str(e))
                                        else:
                                            print(str(i_1) + " no email business")
                                except Exception as e:
                                    print("There is an error connection at url_page : " + str(e))
                        except Exception as e:
                            print("There is an error connection at url : " + str(e))

                        i += 1
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
