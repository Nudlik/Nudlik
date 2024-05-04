from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class EnumParseData:
    """ Класс для хранения данных парсинга """

    url: str
    file_name: str
    tag: str
    coords_local: tuple
    coords_remote: tuple
