import unittest
import time
from bs4 import BeautifulSoup
import requests


class UnitTestsDataMiningMsn(unittest.TestCase):
    def test_extract_the_headline_of_one_article(self):
        print("test_extract_the_headline_of_one_article")

        url_for_one_article = 'https://www.msn.com/fr-fr/actualite/france/rer-b-les-rames-r%c3%a9frig%c3%a9r%c3%a9es-se-font-toujours-attendre/ar-BB17poSi'

        # Request the content of a page from the url
        html = requests.get(url_for_one_article)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        # print(html.text)

        if soup.find("div", {"class": "articlecontent"}).find("h1") is not None:
            print("Headline : " + soup.find("div", {"class": "articlecontent"}).find("h1").text)
        else:
            print("no")

    def test_extract_the_text_of_one_article(self):
        print("test_extract_the_text_of_one_article")

        url_for_one_article = 'https://www.msn.com/fr-fr/actualite/france/d%c3%a9jeuner-au-travail-devant-son-ordinateur-redevient-temporairement-l%c3%a9gal/ar-BB1dIjjU'

        # Request the content of a page from the url
        html = requests.get(url_for_one_article)

        time.sleep(5)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("p") is not None:
            texte = ""

            try:
                all_p = soup.find_all("p")

                for p in all_p:
                    texte += p.text\
                        .replace('\n', ' ')\
                        .replace('\r', ' ')\
                        .replace('\t', ' ')

                print("Texte : " + texte)
            except Exception as e:
                print('error : ' + str(e))
        else:
            print("no")

    def test_extract_all_articles_in_actualite_from_france(self):
        print('test_extract_all_articles_in_actualite_from_france')

        url = 'https://www.msn.com/fr-fr/actualite'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no div class rc-item")

    def test_extract_all_articles_in_entertainment_from_france(self):
        print('test_extract_all_articles_in_entertainment_from_france')

        url = 'https://www.msn.com/fr-fr/entertainment'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_sport_from_france(self):
        print('test_extract_all_articles_in_sport_from_france')

        url = 'https://www.msn.com/fr-fr/sport'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_finance_from_france(self):
        print('test_extract_all_articles_in_finance_from_france')

        url = 'https://www.msn.com/fr-fr/finance'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_lifestyle_from_france(self):
        print('test_extract_all_articles_in_lifestyle_from_france')

        url = 'https://www.msn.com/fr-fr/lifestyle'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_sante_from_france(self):
        print('test_extract_all_articles_in_sante_from_france')

        url = 'https://www.msn.com/fr-fr/sante'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_cuisine_et_vins_from_france(self):
        print('test_extract_all_articles_in_cuisine_et_vins_from_france')

        url = 'https://www.msn.com/fr-fr/cuisine-et-vins'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_voyage_from_france(self):
        print('test_extract_all_articles_in_voyage_from_france')

        url = 'https://www.msn.com/fr-fr/voyage'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")

    def test_extract_all_articles_in_auto_from_france(self):
        print('test_extract_all_articles_in_voyage_from_france')

        url = 'https://www.msn.com/fr-fr/auto'

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
        }

        # Request the content of a page from the url
        html = requests.get(url, headers=headers)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find("a", {"class": "contentlink"}) is not None:
            all_article = soup.find_all('a', {'class': 'contentlink'})

            i = 1

            for article in all_article:
                try:
                    link = 'https://www.msn.com' + article.get('href')
                    label = article.get('aria-label')

                    x = {
                        'link': link,
                        'label': label
                    }

                    print("article " + str(i))
                    print(x)

                    i += 1
                except Exception as e:
                    print('error : ' + str(e))
        else:
            print("no a class contentlink")


if __name__ == '__main__':
    unittest.main()
