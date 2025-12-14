import requests

from src.get_api import FileWorker, Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self, file_worker):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            # print(vacancies)
            self.vacancies.extend(vacancies)
            self.params["page"] += 1


# if __name__ == "__main__":
#     template = "https: // hh.ru / vacancy / 128725099?hhtmFrom = vacancy_search_list"
#
#     # keyword_ = 'python разработчик junior'
#     keyword_ = "python разработчик middle"
#     # keyword_ = 'python разработчик senior'
#     worker = FileWorker("vacancies.json")
#     hh_parser = HH(worker)
#     hh_parser.load_vacancies(keyword_)
#     print(f"Загружено вакансии: {len(hh_parser.vacancies)}")  # 117, 268, 955 14/12/2025
#     my_salary = 150000
#     for i in range(len(hh_parser.vacancies)):
#         if (
#             "salary" in hh_parser.vacancies[i]
#             and hh_parser.vacancies[i]["salary"] is not None
#         ):
#             if hh_parser.vacancies[i]["salary"]["from"] is None:
#                 salary1 = 0
#             else:
#                 salary1 = hh_parser.vacancies[i]["salary"]["from"]
#
#             if hh_parser.vacancies[i]["salary"]["to"] is None:
#                 salary2 = 500000
#             else:
#                 salary2 = hh_parser.vacancies[i]["salary"]["to"]
#
#             salary = hh_parser.vacancies[i]["salary"]
#             if salary1 < my_salary < salary2:
#                 print(hh_parser.vacancies[i]["name"])
#                 print(
#                     f"https://hh.ru/vacancy/{hh_parser.vacancies[i]['id']}?hhtmFrom=vacancy_search_list"
#                 )
