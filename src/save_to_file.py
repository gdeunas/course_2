from abc import ABC

from src.get_api import Parser


class SaveToFile(Parser, ABC):
    """save to file"""

    def SaveToJson(self):
        """save to json"""

    @staticmethod
    def save_to_json():
        pass

    def SaveToXL(self):
        """save to xl"""

    pass
