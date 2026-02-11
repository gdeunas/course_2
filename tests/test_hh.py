import pytest
import requests_mock
from src.hh import HH


@pytest.fixture
def hh_client():
    return HH(file_worker="test_vacancies.json")


def test_load_vacancies_success(hh_client):
    with requests_mock.Mocker() as m:
        mock_data = {"items": [{"id": "1", "name": "Python Developer"}]}

        m.get("https://api.hh.ru/vacancies", json=mock_data, status_code=200)

        hh_client.params["page"] = 19

        result = hh_client.load_vacancies("python")

        assert len(result) > 0
        assert result[0]["name"] == "Python Developer"


def test_load_vacancies_status_error(hh_client, capsys):
    with requests_mock.Mocker() as m:
        m.get("https://api.hh.ru/vacancies", status_code=404)

        hh_client.load_vacancies("python")

        captured = capsys.readouterr()
        assert "404" in captured.out
