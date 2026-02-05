import pytest
from src.vacancy import Vacancy


@pytest.fixture
def sample_data():
    """Фикстура с имитацией ответа от HH API"""
    return [
        {
            "id": "101",
            "name": "Python Developer",
            "area": {"name": "Казань"},
            "salary": {"from": 60000, "currency": "RUR"},
            "experience": {"id": "noExperience"},
            "type": {"id": "open"},
            "employer": {"name": "Tech Corp"}
        },
        {
            "id": "102",
            "name": "Java Developer",
            "area": {"name": "Москва"},
            "salary": {"from": 100000, "currency": "RUR"},
            "experience": {"id": "between1And3"},
            "type": {"id": "open"},
            "employer": {"name": "IT World"}
        },
        {
            "id": "103",
            "name": "Junior Dev",
            "area": {"name": "Казань"},
            "salary": {"from": 30000, "currency": "RUR"},  # Маленькая зарплата
            "experience": {"id": "noExperience"},
            "type": {"id": "open"},
            "employer": {"name": "StartUp"}
        }
    ]


def test_get_data_filtering(sample_data):
    """Тест корректности фильтрации по городу и зарплате"""
    v = Vacancy(sample_data)
    result = v.get_data(city_filter="Казань", salary_from="50000")

    assert len(result) == 1
    assert result[0]["id"] == "101"
    assert result[0]["salary"] == "60000 RUR"


def test_get_data_no_results(sample_data):
    """Тест случая, когда вакансии не найдены"""
    v = Vacancy(sample_data)
    result = v.get_data(city_filter="Казань", experience="moreThan6")
    assert result == []


def test_show_data_output(sample_data, capsys):
    """Тест вывода в консоль через show_data"""
    v = Vacancy(sample_data)
    v.show_data(city_filter="Казань", salary_from="50000")
    captured = capsys.readouterr()
    assert "Python Developer" in captured.out
    assert "Tech Corp" in captured.out
    assert "https://hh.ru" in captured.out


def test_empty_city_default(sample_data):
    """Тест дефолтного значения города, если передан None/пустая строка"""
    v = Vacancy(sample_data)
    result = v.get_data(city_filter="")
    assert all(res["area"] == "Казань" for res in result)

