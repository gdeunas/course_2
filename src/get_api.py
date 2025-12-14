from abc import ABC, abstractmethod

import requests


class GetApi(ABC):
    """abstract class to get api"""

    pass


class GetApiHH(GetApi):
    """get api HH"""

    @staticmethod
    def get_api():
        pass


class Parser1:
    """parser api"""

    @staticmethod
    def get_api():
        url_get = "https://api.hh.ru/vacancies"
        response = requests.get(url_get)
        if response.status_code == 200:
            print(response.json())

    @staticmethod
    def post_api():
        url_post = "https://api.hh.ru/vacancies"
        response = requests.post(url_post)
        if response.status_code == 200:
            print(response.json())
        else:
            print("code= ", response.status_code)


class Parser(ABC):
    """
    Абстрактный базовый класс для парсеров вакансий.
    Определяет общий интерфейс для работы с API и файлами.
    """

    def __init__(self, file_worker):
        # file_worker предполагается объектом, который умеет сохранять и читать данные.
        self.file_worker = file_worker
        self.vacancies = []

    @abstractmethod
    def load_vacancies(self, keyword):
        """
        Абстрактный метод для загрузки вакансий по ключевому слову.
        Должен быть реализован в дочерних классах (например, HH, SuperJob).
        """
        pass

    def save_to_file(self):
        """
        Общий метод для сохранения загруженных вакансий в файл с помощью file_worker.
        """
        self.file_worker.write_data(self.vacancies)

    def load_from_file(self):
        """
        Общий метод для загрузки вакансий из файла с помощью file_worker.
        """
        self.vacancies = self.file_worker.read_data()


class FileWorker:
    """file worker class"""

    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        """write data to file"""
        pass

    def read_data(self):
        """read data from file"""
        pass


if __name__ == "__main__":
    Parser1.post_api()
