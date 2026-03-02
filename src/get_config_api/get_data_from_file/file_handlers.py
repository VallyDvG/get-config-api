import json
from src.get_config_api.get_data_from_file.base import FileHandler


class JSONFileHandler(FileHandler):

    def read_file(self, file_path: str) -> list[dict]:
        """Return json data from file_path"""

        with open(file_path, mode="r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        return data


class CSVFileHandler(FileHandler):
    def read_file(self, file_path: str) -> dict:
        pass


class ExcelFileHandler(FileHandler):
    def read_file(self, file_path: str) -> dict:
        pass


class DOCXFileHandler(FileHandler):
    def read_file(self, file_path: str) -> list[dict]:
        pass


if __name__ == '__main__':
    from src.get_config_api.settings import get_settings

    settings_obj = get_settings()

    json_handler = JSONFileHandler()
    data = json_handler.read_file(settings_obj.DATA_DIR / "network_elements_data.json")
    print(type(data))

