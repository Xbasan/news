from ria_ru import RiaNews
from habr import HabrNews


class HabrNews(HabrNews):
    def __init__(self):
        super().__init__()


class RiaNews(RiaNews):
    def __init__(self):
        super().__init__()


class News():
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    RiaNews()
    News()
