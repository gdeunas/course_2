import json
import os
from abc import ABC, abstractmethod
from typing import Any


class STF(ABC):
    """save to  file abstract class"""

    @abstractmethod
    def get_data_from_file(self):
        """get data from file"""
        pass

    @abstractmethod
    def add_data_to_file(self, data: Any):
        """add data from file"""
        pass

    @abstractmethod
    def del_data_from_file(self, del_data: Any):
        """delete data from file"""
        pass


class FileJson(STF):
    def __init__(self, file_name: str = "vacancy.json") -> None:
        self.__file_name = file_name

    def get_data_from_file(self) -> list[dict[str, Any]]:
        """Get all data from file."""
        file_path = self.__file_name
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def add_data_to_file(self, data: Any) -> None:
        """Add data if ID doesn't exist."""
        file_path = self.__file_name
        existing_data = self.get_data_from_file()
        existing_ids = {item["id"] for item in existing_data}

        if isinstance(data, dict):
            items_to_add = [data]
        elif isinstance(data, list):
            items_to_add = data
        else:
            print("Invalid data type: expected dict or list")
            return

        for item in items_to_add:
            if item.get("id") not in existing_ids:
                existing_data.append(item)
            else:
                print(f"ID {item['id']} already exists")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

    def del_data_from_file(self, del_id: Any) -> None:
        """Delete data by ID."""
        file_path = self.__file_name
        data = self.get_data_from_file()
        data = [item for item in data if item["id"] != del_id]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    pass
