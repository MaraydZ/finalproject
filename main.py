import sqlite3
import requests
from bs4 import BeautifulSoup
from bottle import Bottle, run, template, request, redirect, post

app = Bottle()

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
    
    def get_websites(self):
        self.cursor.execute("SELECT * FROM websites")
        return self.cursor.fetchall()
    

class WebsiteParser:
    def __init__(self):
        pass

    def search_keywords(self, url, keywords):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text().lower()
            counts = {keyword: text.count(keyword.lower()) for keyword in keywords}
            return counts
        return {keyword: 0 for keyword in keywords}

@app.route('/')
def index():
    return template('index')

@app.route('/add_website', method='POST')
def add_website():
    url = request.forms.get('url')
    if url:
        database.add_website(url)
        return redirect('/')
    else:
        return "Введите URL сайта."

@app.route('/clear_database', method='POST')
def clear_database():
    database.clear_database()
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
    keywords_str = request.forms.get('keywords')
    keywords = [keyword.strip() for keyword in keywords_str.split(',')]
    if keywords:
        websites = database.get_websites()
        if not websites:
            return "База данных пуста. Добавьте сайты для поиска."
        results = []
        for website in websites:
            url = website[1]
            counts = website_parser.search_keywords(url, keywords)
            results.append((url, counts))
        
        results.sort(key=lambda x: sum(x[1].values()), reverse=True)
        
        return template('search_results', results=results)
    else:
        return "Введите ключевые слова для поиска (через запятую)."


if __name__ == '__main__':
    database = Database("websites.db")
    website_parser = WebsiteParser()
    run(app, host='localhost', port=8080)
