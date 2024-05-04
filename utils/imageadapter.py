from abc import ABC
from dataclasses import dataclass

import PIL
from PIL.Image import Image


@dataclass(eq=False)
class ImageInterface(ABC):
    """ Интерфейс для работы с изображениями """
    open_provider: None


@dataclass(eq=False)
class ImageAdapter(ImageInterface, Image):
    """ Класс адаптер для работы с изображениями """
    open_provider: PIL.Image.open
