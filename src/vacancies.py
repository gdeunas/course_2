from src.get_api import FileWorker
from src.hh import HH


class Vacancies:
    """get vacancies"""

    def __init__(self):
        self.vacancies = []

    @staticmethod
    def get_data(city_filter='Москва', salary_from='50000', currency='RUR', experience='noExperience', type_id='open',
                 keyword='python разработчик junior'):
        """filtered data
        experiece = ['noExperience', 'between1And3','between3And6', 'moreThan6']
        currency = ['RUR', 'USD']
        """
        # template = "https: // hh.ru / vacancy / 128725099?hhtmFrom = vacancy_search_list"

        # keyword = 'python разработчик junior'
        # "python разработчик middle", 'python разработчик senior'
        salary_from = int(salary_from)
        worker = FileWorker("vacancies_py.json")
        hh_parser = HH(worker)
        hh_parser.load_vacancies(keyword)
        hh_parser.load_vacancies(keyword)
        # print(f"Загружено вакансии: {len(hh_parser.vacancies)}")  # j117, m268, s955 14/12/2025
        for i in range(len(hh_parser.vacancies)):
            if hh_parser.vacancies[i]['area']['name'] == city_filter:
                salary_info = hh_parser.vacancies[i]['salary']
                if salary_info:
                    if salary_info.get('currency') == currency:
                        if hh_parser.vacancies[i]['experience']['id'] == experience and hh_parser.vacancies[i]['type']['id'] == type_id:
                            if (
                                    "salary" in hh_parser.vacancies[i]
                                    and hh_parser.vacancies[i]["salary"] is not None
                            ):
                                if hh_parser.vacancies[i]["salary"]["from"] is None:
                                    salary1 = 0
                                else:
                                    salary1 = hh_parser.vacancies[i]["salary"]["from"]

                                if hh_parser.vacancies[i]["salary"]["to"] is None:
                                    salary2 = 500000
                                else:
                                    salary2 = hh_parser.vacancies[i]["salary"]["to"]

                                if salary_from < salary1:
                                    print(hh_parser.vacancies[i]["name"])
                                    print(
                                        f"https://hh.ru/vacancy/{hh_parser.vacancies[i]['id']}?hhtmFrom=vacancy_search_list"
                                    )


if __name__ == '__main__':
    print("Идет поиск вакансии...")
    Vacancies.get_data()
    print("Поиск вакансии завершен")
