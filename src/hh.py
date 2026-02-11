from typing import Any

import requests

from src.get_api import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self, file_worker: str) -> None:
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies: list[dict[str, Any]] = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str) -> list[dict[str, Any]]:
        """load vacancies from url"""
        if not keyword:
            keyword = "питон"
        self.params["text"] = keyword
        response = requests.get(self.url)
        if response.status_code == 200:
            while self.params.get("page") != 20:
                response = requests.get(self.url, headers=self.headers, params=self.params)  # type: ignore[arg-type]
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1  # type: ignore[operator]
        else:
            print(f"{response.status_code}")

        return self.vacancies
