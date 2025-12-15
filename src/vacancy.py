from typing import Any


class Vacancy:
    """class Vacancies"""

    __slots__ = [
        "hh",
    ]

    def __init__(
        self,
        hh: list[dict[str, Any]],
    ) -> None:
        self.hh = hh

    def get_data(
        self,
        city_filter: str = "Москва",
        salary_from: str = "50000",
        currency: str = "RUR",
        experience: str = "noExperience",
        type_id: str = "open",
    ) -> list[dict[str, Any]]:
        """filtered data
        city_filter=['Москва', 'Казань',...]
        experience = ['noExperience', 'between1And3','between3And6', 'moreThan6']
        currency = ['RUR', 'USD', 'KZT']
        """
        # salary_from = int(salary_from)
        # file_data = ""

        # worker = FileWorker("vacancies_py.json")
        # hh_parser = HH(worker)
        # hh_parser.load_vacancies(keyword)
        # print(f"Загружено вакансии: {len(hh_parser.vacancies)}")  # j117, m268, s955 14/12/2025

        # for i in range(len(self.hh)):

        # if hh[i]["area"]["name"] == city_filter:
        #     salary_info = hh[i]["salary"]
        #     if salary_info:
        #         if salary_info.get("currency") == currency:
        #             if (
        #                 hh[i]["experience"]["id"] == experience
        #                 and hh[i]["type"]["id"] == type_id
        #             ):
        #                 if "salary" in hh[i] and hh[i]["salary"] is not None:
        #                     if hh[i]["salary"]["from"] is None:
        #                         salary1 = 0
        #                     else:
        #                         salary1 = hh[i]["salary"]["from"]
        #                     if salary_from < salary1:
        #                         print(hh[i]["name"])
        #                         print(
        #                             f"https://hh.ru/vacancy/{hh[i]['id']}?hhtmFrom=vacancy_search_list"
        #                         )
        #                         file_data = f"{hh[i]["name"]}"
        salary_from_int = int(salary_from)
        filtered_vacancies = []

        for vacancy in self.hh:
            area_name = vacancy.get("area", {}).get("name")
            if area_name != city_filter:
                continue
            salary_info = vacancy.get("salary", {})
            if not salary_info or salary_info.get("currency") != currency:
                continue
            if (
                vacancy.get("experience", {}).get("id") != experience
                or vacancy.get("type", {}).get("id") != type_id
            ):
                continue
            vacancy_salary = salary_info.get("from") or 0
            if salary_from_int <= vacancy_salary:
                vacancy_info = {
                    "name": vacancy["name"],
                    "salary": f"{salary_info.get('from', 0)} {currency}",
                    "employer": vacancy.get("employer", {}).get("name", "N/A"),
                    "url": f"https://hh.ru/vacancy/{vacancy['id']}",
                    "area": area_name,
                }
                filtered_vacancies.append(vacancy_info)
                # Вывод в консоль
                print(f"{vacancy['name']}")
                print(f"{salary_info.get('from', 0)} {currency}")
                print(f"{vacancy.get('employer', {}).get('name', 'N/A')}")
                print(f"{vacancy_info['url']}")
                # print(f"https://hh.ru/vacancy/{vacancy.get('id')}?hhtmFrom=vacancy_search_list")
                print("-" * 60)

        return filtered_vacancies


# if __name__ == "__main__":
#     print("Идет поиск вакансии...")
#     Vacancy.get_data()
#     print("Поиск вакансии завершен")
