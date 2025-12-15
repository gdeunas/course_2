from src.hh import HH
from src.vacancy import Vacancy

if __name__ == "__main__":
    # 0. Ask user:
    keyword_input = input("Введите ключевое слово для поиска вакансии: ")
    show_console = input("Вывести вакансии в консоль, да или нет? ")
    city_filter = input("Введите город для поиска: ")
    if not city_filter:
        city_filter="Казань"
    print("Идет поиск вакансии...")

    # 1. Get data from Api requests
    vacancy_data = HH("fw").load_vacancies(keyword_input)

    # 2.Filtered data
    filtered_data = Vacancy(vacancy_data)
    if show_console.lower() == "да":
        filtered_data.show_data(city_filter=city_filter)
    else:
        vacancy_filtered = filtered_data.get_data(city_filter=city_filter)
    print("Поиск вакансии завершен!")

    # 3. Store json to file
    # saved = SaveToJson.save_to_json()
