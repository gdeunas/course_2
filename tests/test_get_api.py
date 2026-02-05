import pytest
from src.get_api import Parser, FileWorker


def test_file_worker_init():
    """Проверяем корректную инициализацию FileWorker"""
    filename = "test_vacancies.json"
    worker = FileWorker(filename)
    assert worker.filename == filename


class MockParser(Parser):
    """Временный класс для тестирования абстрактного родителя"""
    def load_vacancies(self, keyword: str):
        return [{"name": "Python Developer"}]


def test_parser_init():
    """Проверяем, что базовый класс корректно сохраняет параметры"""
    file_path = "data.json"
    parser = MockParser(file_path)
    assert parser.file_worker == file_path
    assert parser.vacancies == []


def test_parser_abstract_error():
    """Проверяем, что нельзя создать экземпляр Parser напрямую"""
    with pytest.raises(TypeError):
        Parser("some_file.json")


def test_mock_parser_load():
    """Проверяем реализацию метода в дочернем классе"""
    parser = MockParser("test.json")
    result = parser.load_vacancies("python")
    assert isinstance(result, list)
    assert result[0]["name"] == "Python Developer"
