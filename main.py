from src.hh import HH
from src.vacancy import Vacancy

if __name__ == "__main__":
    # 1. Get data from Api requests
    print("Идет поиск вакансии...")
    vacancy_data = HH("fw").load_vacancies("Python")

    # 2.Filtered data
    filtered_data = Vacancy(vacancy_data)
    vacancy_filtered = filtered_data.get_data(city_filter="Казань")
    # filtered_data.show_data(city_filter="Казань")
    print("Поиск вакансии завершен!")

    # 3. Store json to file
    # saved = SaveToJson.save_to_json()
