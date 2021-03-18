import time
import unittest
from bs4 import BeautifulSoup
import requests


class UnitTestsDataMiningLeboncoin(unittest.TestCase):
    def test_extract_the_title_of_the_ad(self):
        print('test_extract_the_title_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("h1", {"data-qa-id": "adview_title"}) is not None:
                    title = soup.find("h1", {"data-qa-id": "adview_title"}).text
                    print("title : " + title)
                else:
                    print("no title")
            except Exception as e:
                print("error title : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_price_of_the_ad(self):
        print('test_extract_the_price_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"data-qa-id": "adview_price"}) is not None:
                    price = soup.find("div", {"data-qa-id": "adview_price"}).text
                    print("price : " + price)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_location_of_the_ad(self):
        print('test_extract_the_location_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"class": "css-iel3r1"}) is not None:
                    location_city = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[1].split(" ")[0].replace(" ", "")
                    location_postal_code = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[1].split(" ")[1].replace(" ", "")
                    print("location_city : " + location_city + " / location_postal_code : " + location_postal_code)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_the_surface_of_the_ad(self):
        print('test_extract_the_surface_of_the_ad')

        try:
            url_ad = 'https://www.leboncoin.fr/ventes_immobilieres/1930964997.htm?ac=558505705'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': url_ad.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(url_ad, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("div", {"class": "css-iel3r1"}) is not None:
                    surface = soup.find("div", {"class": "css-iel3r1"}).text.split("·")[0]
                    print("surface : " + surface)
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_ads_from_one_page(self):
        print('test_extract_all_ads_from_one_page')

        try:
            urls_ads_from_one_page = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&square=500-max&page=1'

            headers = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_one_page.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session',
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_one_page, headers=headers)

            # Parse the content of html_doc
            soup = BeautifulSoup(response.text, 'html.parser')

            try:
                if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                    all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                    for i in range(0, len(all_a)):
                        print("ad " + str(i) + " : https://www.leboncoin.fr" + all_a[i].get("href"))
                else:
                    print("no price")
            except Exception as e:
                print("error price : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))

    def test_extract_all_ads_from_all_pages(self):
        print('test_extract_all_ads_from_all_pages')

        cookie = '__Secure-InstanceId=cc56ea7d-a44d-47cb-a2f3-1305700071a7; atidvisitor=%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-562498-%22%2C%22an%22%3A%22NaN%22%2C%22ac%22%3A%22%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwiZXhwIjoxNjQ3NjAyNDYwODgzLCJjcyI6bnVsbH0%3D; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5XzdGQ0FEMzgyLTVFOEQtNDlGOC1CNzY5LTI3OTg1MzUyNkZCRSIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; uuid=8d770939-aa5f-43a3-a355-33ded9f62220; user_search_config={"sort_by":"price","sort_order":"desc"}; datadome=O.sju8RJyX62RZhkFcj9BD~yGZT4omiTF5kP~bo9fL~FRF8YIEBDMLF1QbZ.j_sARHkflTAwSibodP~JqQSgjTXUL1YJdEm2F_YTBxqGud; utag_main=v_id:017845113865001f64e88cefdc9103082001907a0086e$_sn:2$_ss:0$_st:1616082152219$_pn:8%3Bexp-session$ses_id:1616080197381%3Bexp-session'

        try:
            urls_ads_from_page_one = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&square=500-max&page=1'

            headers_urls_ads_from_one_page = {
                'authority': 'www.leboncoin.fr',
                'method': 'GET',
                'path': urls_ads_from_page_one.replace('https://www.leboncoin.fr', ''),
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'cache-control': 'max-age=0',
                'cookie': cookie,
                'dnt': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
            }

            # Request the content of a page from the url
            response = requests.get(urls_ads_from_page_one, headers=headers_urls_ads_from_one_page)

            # Parse the content of html_doc
            soup_urls_ads_from_one_page = BeautifulSoup(response.text, 'html.parser')

            number_of_pages = 0

            if soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"}) is not None:
                number_of_pages_with_coma = int(soup_urls_ads_from_one_page.find("span", {"class": "_3Ce01 _137P- P4PEa _35DXM"})
                                                .text
                                                .replace(" ", "")
                                                .replace("results", "")
                                                ) / 35

                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                    number_of_pages += round(number_of_pages_with_coma) + 1
                    print('number_of_pages : ' + str(number_of_pages))
                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                    number_of_pages += round(number_of_pages_with_coma)
                    print('number_of_pages : ' + str(number_of_pages))
            else:
                print("error pages")

            try:
                for i_page in range(1, number_of_pages + 1):
                    urls_ads_from_one_page = 'https://www.leboncoin.fr/recherche?category=9&locations=r_12&real_estate_type=3&square=500-max&page=' + str(i_page)

                    print(urls_ads_from_one_page)

                    headers_urls_ads_from_one_page = {
                        'authority': 'www.leboncoin.fr',
                        'method': 'GET',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'cache-control': 'max-age=0',
                        'cookie': cookie,
                        'dnt': '1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
                    }

                    time.sleep(2)

                    # Request the content of a page from the url
                    response = requests.get(urls_ads_from_one_page, headers=headers_urls_ads_from_one_page)

                    # Parse the content of html_doc
                    soup = BeautifulSoup(response.text, 'html.parser')

                    if soup.find("a", {"data-qa-id": "aditem_container"}) is not None:
                        all_a = soup.find_all("a", {"data-qa-id": "aditem_container"})

                        for i in range(0, len(all_a)):
                            print("ad " + str(i) + " : https://www.leboncoin.fr" + all_a[i].get("href"))
                    else:
                        print("no a data-qa-id aditem_container")
            except Exception as e:
                print("error for : " + str(e))
        except Exception as e:
            print("error request url_ad : " + str(e))


if __name__ == '__main__':
    unittest.main()
