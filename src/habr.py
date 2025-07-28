import requests
from bs4 import BeautifulSoup


class HabrNews():
    def __init__(self):
        super().__init__()

        self._url = "https://habr.com"
        self.region = "ru"
        self.res_list = list()
        self._res_list_posts = list()

    def pars_posts(self):
        url_post = f"{self._url}/flows/develop/posts/"
        for page in range(1, 50):
            req = requests.get(f"{url_post}/page{page}/").text
        soup = BeautifulSoup(req, "lxml")

        post_list = soup.find_all("div", class_="tm-post-snippet")

        for post_atem in post_list:
            author = self._author_pars(post_atem)
            topic = self._tm(post_atem)
            text = self._text(post_atem)
            paper = self.pars_news()

            self._res_list_posts.append(
                {
                    "author": author,
                    "topic": topic,
                    "text": text,
                    "paper": paper,
                    # "img": img,
                }
            )

    def pars_news(self):
        req = requests.get(self._url).text
        soup = BeautifulSoup(req, "lxml")

        news_list = soup.find_all("article", class_="tm-articles-list__item")

        for news_atem in news_list:
            author = self._author_pars(news_atem)
            topic = self._tm(news_atem)
            title = self._title(news_atem)
            paper = title[1]
            img = self._img_url(news_atem)

            self.res_list.append(
                {
                    "author": author,
                    "teg": topic,
                    "title": title[0],
                    "paper": paper,
                    "img": img,
                }
            )

    def _text(self, lxml):
        res = list()
        class_ = "article-formatted-body article-formatted-body article-formatted-body_version-2"
        div = lxml.find("div", class_=class_)

        p = div.find_all("p")

        for tx in p:
            text = tx.get_text(strip=True)
            if text:
                res.append(text)

        return res

    def _tm(self, lxml):
        res = list()
        tegs = lxml.find_all("span",
                             class_="tm-publication-hub__link-container")

        for teg in tegs:
            res.append(teg.text)

        return res

    def _author_pars(self, lxml):
        a = lxml.find("a", class_="tm-user-info__username")
        if a:
            return {
                "name": a.text,
                "author_url": f"{self._url}{a.get('href')}"
            }
        else:
            return [None, None]

    def _title(self, lmxl):
        a = lmxl.find("a", class_="tm-title__link")
        if a:
            return [a.get_text(strip=True), f"{self._url}{a.get('href')}"]
        else:
            return [None, None]

    def _img_url(self, lmxl):
        img = lmxl.find("div",
                        class_="tm-article-snippet__cover tm-article-snippet__cover_cover")
        if img:
            return img.get("src")

    def posts_list(self):
        return self._res_list_posts


if __name__ == "__main__":
    news = HabrNews()
    # news.url()
    # news.pars_news()
    news.pars_posts()

    i = 1
    for n in news.posts_list():
        print(i)
        i += 1
    # print(news.posts_list())
