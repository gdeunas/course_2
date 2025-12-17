from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """
    Абстрактный базовый класс для парсеров вакансий.
    Определяет общий интерфейс для работы с API и файлами.
    """

    def __init__(self, file_worker: str):
        self.file_worker = file_worker
        self.vacancies: list[dict] = []

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict[str, Any]]:
        """
        Абстрактный метод для загрузки вакансий по ключевому слову.
        Должен быть реализован в дочерних классах (например, HH, SuperJob).
        """
        pass


class FileWorker:
    """file worker class"""

    def __init__(self, filename: str) -> None:
        self.filename = filename
