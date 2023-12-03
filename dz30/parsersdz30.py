import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="productColText")
        for item in news:
            title = item.find("span", class_="middle").text.strip()
            rub = item.find("a", class_="price").text
            html = item.find("a")["href"]
            self.res.append({
                'title': title,
                'rub': rub,
                'html': html
            })

    def write_save(self):
        with open(self.path, "w") as f:
            a = 1
            for item in self.res:
                f.write(f"Покупка №{a}\nНазвание:{item['title']}\nЦена:{item['rub']}\nСсылка:{item['html']}\n\n\n")
                a += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.write_save()


