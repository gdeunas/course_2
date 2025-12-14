from src.get_api import GetApiHH
from src.save_to_file import SaveToJson
from src.vacancies import GetVacancies

if __name__ == "__main__":
    getdata = GetApiHH.get_api()

    filtered_data = GetVacancies.filter_data()

    saved = SaveToJson.save_to_json()
