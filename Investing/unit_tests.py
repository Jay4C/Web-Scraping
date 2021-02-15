import unittest
import time
from bs4 import BeautifulSoup
import requests


# https://www.investing.com/
class UnitTestsDataMiningInvesting(unittest.TestCase):
    # https://www.investing.com/news/latest-news
    def test_extract_latest_news(self):
        print('test_extract_latest_news')

        url = 'https://www.investing.com/news/latest-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("article") is not None:
            all_article = soup.find_all("article")

            i = 1

            for article in all_article:
                try:
                    url_article = "https://www.investing.com" + article\
                        .find('div', {'class': 'textDiv'})\
                        .find('a')\
                        .get('href')

                    title = article\
                        .find('div', {'class': 'textDiv'})\
                        .find('a')\
                        .text

                    dict_article = {
                        'url_article': url_article,
                        'title': title
                    }

                    print('article : ' + str(i))
                    print(dict_article)
                    i += 1
                except Exception as e:
                    print('error : ' + str(e))

    # https://www.investing.com/news/most-popular-news
    def test_extract_most_popular_news(self):
        print('test_extract_most_popular_news')

        url = 'https://www.investing.com/news/most-popular-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("article") is not None:
            all_article = soup.find_all("article")

            i = 1

            for article in all_article:
                try:
                    url_article = "https://www.investing.com" + article\
                        .find('div', {'class': 'textDiv'})\
                        .find('a')\
                        .get('href')

                    title = article\
                        .find('div', {'class': 'textDiv'})\
                        .find('a')\
                        .text

                    dict_article = {
                        'url_article': url_article,
                        'title': title
                    }

                    print('article : ' + str(i))
                    print(dict_article)
                    i += 1
                except Exception as e:
                    print('error : ' + str(e))

    # https://www.investing.com/news/cryptocurrency-news
    def test_extract_cryptocurrency_news(self):
        print('test_extract_cryptocurrency_news')

        url = 'https://www.investing.com/news/cryptocurrency-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 2056):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/stock-market-news
    def test_extract_stock_market_news(self):
        print('test_extract_stock_market_news')

        url = 'https://www.investing.com/news/stock-market-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 10506):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/commodities-news
    def test_extract_commodities_news(self):
        print('test_extract_stock_market_news')

        url = 'https://www.investing.com/news/commodities-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 2081):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/forex-news
    def test_extract_forex_news(self):
        print('test_extract_forex_news')

        url = 'https://www.investing.com/news/forex-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 4327):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/economy
    def test_extract_economy_news(self):
        print('test_extract_forex_news')

        url = 'https://www.investing.com/news/economy'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 2693):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/economic-indicators
    def test_extract_economic_indicators_news(self):
        print('test_extract_economic_indicators_news')

        url = 'https://www.investing.com/news/economic-indicators'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 1822):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/politics
    def test_extract_news_politics(self):
        print('test_extract_news_politics')

        url = 'https://www.investing.com/news/politics'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 1358):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/news/world-news
    def test_extract_world_news(self):
        print('test_extract_world_news')

        url = 'https://www.investing.com/news/world-news'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        for x in range(1, 6923):
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))

    # https://www.investing.com/analysis/most-popular-analysis
    def test_extract_analysis_most_popular_analysis(self):
        print('test_extract_analysis_most_popular_analysis')

        url = 'https://www.investing.com/analysis/most-popular-analysis'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("article") is not None:
            all_article = soup.find_all("article")

            for article in all_article:
                try:
                    url_article = "https://www.investing.com" + article \
                        .find('div', {'class': 'textDiv'}) \
                        .find('a') \
                        .get('href')

                    title = article \
                        .find('div', {'class': 'textDiv'}) \
                        .find('a') \
                        .text

                    dict_article = {
                        'url_article': url_article,
                        'title': title
                    }

                    print('article : ' + str(i))
                    print(dict_article)
                    i += 1
                except Exception as e:
                    print('error : ' + str(e))

    # https://www.investing.com/analysis/editors-picks
    def test_extract_analysis_editors_picks(self):
        print('test_extract_analysis_editors_picks')

        url = 'https://www.investing.com/analysis/editors-picks'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/market-overview
    def test_extract_analysis_market_overview(self):
        print('test_extract_analysis_market_overview')

        url = 'https://www.investing.com/analysis/market-overview'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/stock-markets
    def test_extract_analysis_stock_markets(self):
        print('test_extract_analysis_stock_markets')

        url = 'https://www.investing.com/analysis/stock-markets'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/forex
    def test_extract_analysis_forex(self):
        print('test_extract_analysis_forex')

        url = 'https://www.investing.com/analysis/forex'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/commodities
    def test_extract_analysis_commodities(self):
        print('test_extract_analysis_commodities')

        url = 'https://www.investing.com/analysis/commodities'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/cryptocurrency
    def test_extract_analysis_cryptocurrency(self):
        print('test_extract_analysis_cryptocurrency')

        url = 'https://www.investing.com/analysis/cryptocurrency'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/bonds
    def test_extract_analysis_bonds(self):
        print('test_extract_analysis_bonds')

        url = 'https://www.investing.com/analysis/bonds'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/etfs
    def test_extract_analysis_etfs(self):
        print('test_extract_analysis_etfs')

        url = 'https://www.investing.com/analysis/etfs'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1

    # https://www.investing.com/analysis/comics
    def test_extract_analysis_comics(self):
        print('test_extract_analysis_comics')

        url = 'https://www.investing.com/analysis/comics'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        i = 1

        x = 1

        while True:
            # Request the content of a page from the url
            html = requests.get(url + '/' + str(x), headers=headers)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find("article") is not None:
                all_article = soup.find_all("article")

                for article in all_article:
                    try:
                        url_article = "https://www.investing.com" + article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .get('href')

                        title = article\
                            .find('div', {'class': 'textDiv'})\
                            .find('a')\
                            .text

                        dict_article = {
                            'url_article': url_article,
                            'title': title
                        }

                        print('article : ' + str(i))
                        print(dict_article)
                        i += 1
                    except Exception as e:
                        print('error : ' + str(e))
            else:
                break

            x += 1


if __name__ == '__main__':
    unittest.main()
