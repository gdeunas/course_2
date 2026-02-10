from typing import Any


class Vacancy:
    """class Vacancies"""

    __slots__ = [
        "hh",
        "city_filter",
        "salary_from",
        "currency",
        "experience",
        "type_id",
        "text"
    ]

    def __init__(
            self,
            hh: list[dict[str, Any]],
            city_filter: str = "Казань",
            salary_from: str = "50000",
            currency: str = "RUR",
            experience: str = "noExperience",
            type_id: str = "open",
    ) -> None:
        # Инициализируем данные и фильтры как атрибуты класса
        self.hh = hh
        self.city_filter = city_filter
        self.salary_from = salary_from
        self.currency = currency
        self.experience = experience
        self.type_id = type_id

    def get_data(self) -> list[dict[str, Any]]:
        """filtered data
        city_filter=['Москва', 'Казань',...]
        experience = ['noExperience', 'between1And3','between3And6', 'moreThan6']
        currency = ['RUR', 'USD', 'KZT']
        """

        salary_from_int = int(self.salary_from)
        filtered_vacancies = []

        for vacancy in self.hh:
            area_name = vacancy.get("area", {}).get("name")
            if area_name != self.city_filter:
                continue
            salary_info = vacancy.get("salary", {})
            if not salary_info or salary_info.get("currency") != self.currency:
                continue
            if (
                    vacancy.get("experience", {}).get("id") != self.experience
                    or vacancy.get("type", {}).get("id") != self.type_id
            ):
                continue
            vacancy_salary = salary_info.get("from") or 0
            if salary_from_int <= vacancy_salary:
                vacancy_info = {
                    "id": vacancy.get("id"),
                    "name": vacancy["name"],
                    "salary": f"{salary_info.get('from', 0)} {self.currency}",
                    "employer": vacancy.get("employer", {}).get("name", "N/A"),
                    "url": f"https://hh.ru/vacancy/{vacancy['id']}",
                    "area": area_name,
                }
                filtered_vacancies.append(vacancy_info)
        return filtered_vacancies

    def show_data(self) -> None:
        """Выводит отфильтрованные вакансии в консоль"""
        vacancies = self.get_data()

        if not vacancies:
            print("Вакансии не найдены")
            return

        for vacancy in vacancies:
            print(f"id: {vacancy['id']}")
            print(f"Название: {vacancy['name']}")
            print(f"Зарплата: {vacancy['salary']}")
            print(f"Работодатель: {vacancy['employer']}")
            print(f"Ссылка: {vacancy['url']}")
            print(f"Город: {vacancy['area']}")
            print("-" * 60)
