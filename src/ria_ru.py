import datetime
import requests
from bs4 import BeautifulSoup


class RiaNews():
    def __init__(self):
        super().__init__()

        self.url = "https://ria.ru/services/world"
        self.res_list = list()

    def ria_ru_pars(self):
        req = requests.get(self.url).text

        soup = BeautifulSoup(req, "lxml")

        news_list = soup.find_all("div", class_="list-item")

        for news_atem in news_list:

            url_image = news_atem.find("img",
                                       class_="responsive_img m-list-img"
                                       ).get("src")
            title_text = news_atem.find("a",
                                        class_="list-item__title color-font-hover-only")
            tegs_news = news_atem.find_all("a", class_="m-add")
            news_url = title_text.get("href")

            self.res_list.append(
                {
                    "url_image": url_image,
                    "title_text": title_text.text,
                    "news_url": news_url,
                    "news_teg": self.ria_ru_teg_pars(tegs_news),
                }
            )

    def ria_ru_teg_pars(self, tegs_list):
        res = []
        for teg in tegs_list:
            res.append(teg.text)

        return res

    def ria_ru_url(self):
        date = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        print(date)
        self.url = f"https://ria.ru/services/world/more.html?date={date}"


if __name__ == "__main__":
    news = RiaNews()
    news.ria_ru_url()
    news.ria_ru_pars()

    print(news.res_list)



