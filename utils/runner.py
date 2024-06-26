from abc import abstractmethod, ABC
from dataclasses import dataclass

from utils.enum_parse_data import EnumParseData
from utils.imageadapter import ImageInterface, ImageAdapter
from utils.osadapter import OSInterface, OSAdapter
from utils.screenshot import ScreenShotInterface, ScreenShot


@dataclass(eq=False)
class RunnerInterface(ABC):
    """ Интерфейс для запуска программы """

    screenshot_service: ScreenShotInterface
    image_service: ImageInterface
    os_service: OSInterface

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
    screenshot_service: ScreenShot
    image_service: ImageAdapter
    os_service: OSAdapter

    data: list[dict,]
    REMOTE: bool

    def run(self):
        data = self.dict_to_enum()
        self.download_screenshots(data)
        self.refactor_screenshots(data)

    def download_screenshots(self, data: [EnumParseData]) -> None:
        with self.screenshot_service as browser:
            for item in data:
                browser.make_screenshot(item.url, self.os_service, item.file_name, item.tag)

    def refactor_screenshots(self, data: [EnumParseData]) -> None:
        for item in data:
            path = self.os_service.join_folder_img(item.file_name)
            with self.image_service.open_provider(path) as img:
                cords = item.coords_remote if self.REMOTE else item.coords_local
                with img.crop(cords) as cropped_img:
                    cropped_img.save(self.os_service.join_result_img(item.file_name))

    def dict_to_enum(self) -> [EnumParseData]:
        """ Преобразование словарей в Enum для удобства обращения """
        return [EnumParseData(**item) for item in self.data]
