from src.hh import HH
from src.vacancy import Vacancy
from src.work_with_file import FileJson


def user_interaction():
    # 0. Ask user:
    keyword_input = input("Введите ключевое слово для поиска вакансии: ")
    show_console = input("Вывести вакансии в консоль, да или нет? ")
    city_filter = input("Введите город для поиска: ")
    print("Идет поиск вакансии...")

    # 1. Get data from Api requests
    filename = "vacancy.json"
    vacancy_data = HH(filename).load_vacancies(keyword_input)

    # 2.Filtered data
    filtered_data = Vacancy(vacancy_data)
    vacancy_filtered = filtered_data.get_data(city_filter=city_filter)

    if show_console.lower() == "да":
        filtered_data.show_data(city_filter=city_filter)
    print("Поиск вакансии завершен!")

    # 3. Store json to file
    file_json = FileJson(filename)
    file_json.add_data_to_file(vacancy_filtered)

    # 4. Delete vacancy id '128373566' from file
    # file_json.del_data_from_file('128373566')


if __name__ == "__main__":
    user_interaction()
