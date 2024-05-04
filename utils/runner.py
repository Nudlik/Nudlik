from abc import abstractmethod, ABC
from dataclasses import dataclass

from utils.enum_parse_data import EnumParseData
from utils.imageadapter import ImageInterface, ImageAdapter
from utils.osadapter import OSInterface, OSAdapter
from utils.screenshot import ScreenShotInterface, ScreenShot


@dataclass(eq=False)
class RunnerInterface(ABC):
    """ Интерфейс для запуска программы """

    screenshot_interface: ScreenShotInterface
    image_interface: ImageInterface
    os_interface: OSInterface

    @abstractmethod
    def run(self):
        """ Запуск программы """
        pass

    @abstractmethod
    def download_screenshots(self, data: [EnumParseData]) -> None:
        """ Загрузка скриншотов """
        pass

    @abstractmethod
    def refactor_screenshots(self, data: [EnumParseData]) -> None:
        """ Рефактор скриншотов """
        pass


@dataclass(eq=False)
class Runner(RunnerInterface):
    screenshot_interface: ScreenShot
    image_interface: ImageAdapter
    os_interface: OSAdapter

    data: list[dict,]
    REMOTE: bool

    def run(self):
        data = self.dict_to_enum()
        self.download_screenshots(data)
        self.refactor_screenshots(data)

    def download_screenshots(self, data: [EnumParseData]) -> None:
        with self.screenshot_interface as browser:
            for item in data:
                browser.make_screenshot(item.url, item.file_name, item.tag)

    def refactor_screenshots(self, data: [EnumParseData]) -> None:
        for item in data:
            path = self.os_interface.join_folder_img(item.file_name)
            with self.image_interface.open_provider(path) as img:
                cords = item.coords_remote if self.REMOTE else item.coords_local
                with img.crop(cords) as cropped_img:
                    cropped_img.save(self.os_interface.join_result_img(item.file_name))

    def dict_to_enum(self) -> [EnumParseData]:
        """ Преобразование словарей в Enum для удобства обращения """
        return [EnumParseData(**item) for item in self.data]
