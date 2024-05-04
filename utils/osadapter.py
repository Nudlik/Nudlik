import os as os_default
from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass(eq=False)
class OSInterface(ABC):
    """ Абстрактный интерфейс для работы с файловой системой """
    os: None

    @abstractmethod
    def join(self, *args: (str,)) -> str:
        """ Объединяет пути в один """
        pass

    @abstractmethod
    def join_folder_img(self, *args: (str,)) -> str:
        """ Объединяет пути в один с папкой с изображениями """
        pass

    @abstractmethod
    def join_result_img(self, img_name: str) -> str:
        """ Объединяет пути в один с префиксом для результирующих изображений """
        pass


@dataclass(eq=False)
class OSAdapter(OSInterface):
    os: os_default
    folder_img: str
    prefix_result_img: str

    def join(self, *args: (str,)) -> str:
        return self.os.path.join(*args)

    def join_folder_img(self, *args: (str,)) -> str:
        return self.join(self.folder_img, *args)

    def join_result_img(self, img_name: str) -> str:
        return self.join(self.folder_img, self.prefix_result_img + img_name)
