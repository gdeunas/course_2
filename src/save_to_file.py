from src.get_api import GetApi


class SaveToFile(GetApi):
    """save to file"""

    pass


class SaveToJson(SaveToFile):
    """save to json"""

    @staticmethod
    def save_to_json():
        pass


class SaveToXL(SaveToFile):
    """save to xl"""

    pass
