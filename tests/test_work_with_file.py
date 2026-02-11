import pytest
from src.work_with_file import FileJson


@pytest.fixture
def temp_json_file(tmp_path):
    """Создает временный файл для тестов."""
    file = tmp_path / "test_vacancy.json"
    return str(file)


def test_add_data_to_file(temp_json_file):
    fj = FileJson(temp_json_file)
    data = {"id": 1, "title": "Python Developer"}

    # Тест добавления
    fj.add_data_to_file(data)
    content = fj.get_data_from_file()
    assert len(content) == 1
    assert content[0]["id"] == 1

    # Тест дубликата (не должен добавиться)
    fj.add_data_to_file(data)
    assert len(fj.get_data_from_file()) == 1


def test_del_data_from_file(temp_json_file):
    fj = FileJson(temp_json_file)
    data_list = [{"id": 1}, {"id": 2}]
    fj.add_data_to_file(data_list)

    # Удаляем один элемент
    fj.del_data_from_file(1)
    content = fj.get_data_from_file()
    assert len(content) == 1
    assert content[0]["id"] == 2


def test_get_data_empty_file(temp_json_file):
    fj = FileJson("non_existent.json")
    assert fj.get_data_from_file() == []
