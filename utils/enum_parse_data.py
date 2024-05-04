from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class EnumParseData:
    url: str
    file_name: str
    tag: str
    coords_local: tuple
    coords_remote: tuple
