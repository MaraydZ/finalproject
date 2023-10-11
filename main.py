# Main libraries
from bottle import Bottle, run, template, request, redirect, post
import requests
import re
import html
from bs4 import BeautifulSoup
import sqlite3
import os

class AppConfig:
    def config(self):
        self.address = "localhost"
        self.port = "8080"
        self.start_web_at_run = False

class Hello:
    def __init__(self) -> None:
        pass

    def hello(self, value):
        if value == "hello":
            # print("Hello! It's a Google or Yandex-like search engine.")
            print("Hello! It's a Google-like search engine")
        else:
            pass

class AppRun:
    def __init__(self) -> None:
        self.app_config = AppConfig()
        self.app_config.config()

    def start(self):
        if self.app_config.start_web_at_run:
            os.system(f"start http://{self.app_config.address}:{self.app_config.port}")
        else:
            pass

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS websites (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                url TEXT)''')
        self.conn.commit()

    def add_website(self, url):
        self.cursor.execute("INSERT INTO websites (url) VALUES (?)", (url,))
        self.conn.commit()

    def clear_database(self):
        self.cursor.execute("DELETE FROM websites")
        self.conn.commit()

    def get_all_websites(self):
        self.cursor.execute("SELECT * FROM websites")
        return self.cursor.fetchall()

    def get_search_queries(self):
        self.cursor.execute("SELECT DISTINCT url FROM websites")
        return [row[0] for row in self.cursor.fetchall()]

class WebsiteParser:
    def __init__(self):
        pass

    def search_keywords(self, url, keywords):
        print(keywords)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            counts = {keyword: text.count(keyword.lower()) for keyword in keywords}
            return counts
        return {keyword: 0 for keyword in keywords}

class GoogleSearch:
    def __init__(self):
        pass

    def search(self, query):
        query = "+".join(query)  # Объединить слова в запрос
        url = f"https://google.com/search?q={query}"
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            urls = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http') or href.startswith('https'):
                    decoded_url = html.unescape(href)
                    url_parts = decoded_url.split("\\")
                    cleaned_url = url_parts[0]
                    cleaned_url = cleaned_url.replace('"', '')
                    if not cleaned_url.startswith(('https://www.w3.org', 'https://www.google.com', "https://policies.google.com", "https://accounts.google.com", "https://support.google.com")) \
                                                    and 'google' not in cleaned_url and 'wiki' not in cleaned_url and not 'wikipedia' in cleaned_url \
                                                    and not 'yandex' in cleaned_url and not 'youtube' in cleaned_url:
                        urls.append(cleaned_url)
            return urls
        return []
    def calculate_score(self, url, keywords):
        geted = requests.get(url).text
        soup = BeautifulSoup(geted, 'html.parser')
        score = 0
        scorelol = 0
        if url.startswith("https"):
            scorelol += 10
        elif url.startswith("http"):
            scorelol -= 10

        html_tag = soup.find("html")
        head_tag = soup.find("head")
        body_tag = soup.find("body")

        if html_tag and head_tag and body_tag:
            scorelol += 10
        else:
            scorelol -= 10

        if not keywords:
            scorelol -= 15
        else:
            keyword_counts = website_parser.search_keywords(url, keywords)
            total_keyword_count = sum(keyword_counts.values())
            score += total_keyword_count + scorelol
            print(score)
        return score
        

# class YandexSearch:
#     def __init__(self):
#         pass

#     def search(self, query):
#         query = "+".join(query)  # Объединить слова в запрос
#         url = f"https://yandex.ru/search/?text={query}"
#         print(url)
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
#         }

#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             urls = []
#             for link in soup.find_all('a', href=True):
#                 href = link['href']
#                 if href.startswith('http') or href.startsWith('https'):
#                     decoded_url = html.unescape(href)
#                     url_parts = decoded_url.split("\\")
#                     cleaned_url = url_parts[0]
#                     cleaned_url = cleaned_url.replace('"', '')
#                     if not cleaned_url.startswith(('https://www.w3.org', 'https://www.google.com', "https://policies.google.com", "https://accounts.google.com", "https://support.google.com")) and 'google' not in cleaned_url and 'wiki' not in cleaned_url and not 'wikipedia' in cleaned_url and not 'yandex' in cleaned_url and not 'youtube' in cleaned_url:
#                         urls.append(cleaned_url)
#             return urls
#         return []

#     def calculate_score(self, url, keywords):
#         geted = requests.get(url).text
#         soup = BeautifulSoup(geted, 'html.parser')
#         score = 0
#         print(keywords)
#         scorelol = 0
#         print(url)
#         if url.startswith(f"https"):
#             scorelol += 10
#         elif url.startswith(f"http"):
#             scorelol -= 10

#         html_tag = soup.find("html")
#         head_tag = soup.find("head")
#         body_tag = soup.find("body")

#         if html_tag and head_tag and body_tag:
#             scorelol += 10
#         else:
#             scorelol -= 10

#         if not keywords:
#             score -= 15
#         else:
#             keyword_counts = website_parser.search_keywords(url, keywords)
#             total_keyword_count = sum(keyword_counts.values())
#             score += total_keyword_count + scorelol
#         return score

# Bottle framework. (Web GUI)
app = Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/add_website', method='POST')
def add_website():
    url = request.forms.get('url')
    if url:
        if url not in unique_websites:
            unique_websites.add(url)
            database.add_website(url)
        return redirect('/')
    else:
        return "Введите URL сайта."

@app.route('/clear_database', method='POST')
def clear_database():
    database.clear_database()
    unique_websites.clear()
    return redirect('/')

@app.route('/view_websites')
def view_websites():
    websites = database.get_all_websites()
    if not websites:
        return '<!DOCTYPE html><html><head></head><body><script>alert("База данных пуста!"); location.href = "/"</script></body></html>'
    else:
        return template('view_websites', websites=websites)

@app.route('/search', method='POST')
def search():
    global unique_websites
    database_queries = database.get_search_queries()
    if not database_queries:
        return '<!DOCTYPE html><html><head></head><body><script>alert("База данных запросов пуста. Добавьте запросы для поиска"); location.href = "/"</script></body></html>'
    results = []

    urls = []
    scores = []

    for query in database_queries:
        query_keywords = [keyword.strip() for keyword in query.split(' ')]
        google_results = google_search.search(query_keywords)

        if google_results:
            for result_url in google_results:
                if result_url not in unique_websites:
                    
                    unique_websites.add(result_url)
                    website_keywords = website_parser.search_keywords(result_url, query_keywords)
                    google_search_instance = GoogleSearch()  
                    score = google_search_instance.calculate_score(url=result_url, keywords=query_keywords)
                    urls.append(result_url)
                    scores.append(score)

    results = list(zip(urls, scores))

    results.sort(key=lambda x: x[1], reverse=True)

    return template('search_results', results=results)

# @app.route('/yasearch', method='POST')
# def yasearch():
#     global unique_websites
#     database_queries = database.get_search_queries()
#     if not database_queries:
#         return '<!DOCTYPE html><html><head></head><body><script>alert("База данных запросов пуста. Добавьте запросы для поиска"); location.href = "/"</script></body></html>'
#     results = []

#     urls = []
#     scores = []

#     for query in database_queries:
#         query_keywords = [keyword.strip() for keyword in query.split(' ')]  # Разделить по пробелу
#         yandex_results = yandex_search.search(query_keywords)

#         if yandex_results:
#             for result_url in yandex_results:
#                 if result_url not in unique_websites:
#                     unique_websites.add(result_url)
#                     website_keywords = website_parser.search_keywords(result_url, query_keywords)
#                     score = sum(website_keywords.values())
#                     urls.append(result_url)
#                     scores.append(score)

#     results = list(zip(urls, scores))

#     results.sort(key=lambda x: x[1], reverse=True)

#     return template('search_results', results=results)

if __name__ == '__main__':
    Hello = Hello()
    Hello.hello(value="hello")
    database = Database("websites.db")
    website_parser = WebsiteParser()
    google_search = GoogleSearch()
    # yandex_search = YandexSearch()
    unique_websites = set()
    AppRun = AppRun()
    AppRun.start()
    app_config = AppConfig()
    app_config.config()
    run(app, host=app_config.address, port=app_config.port)
