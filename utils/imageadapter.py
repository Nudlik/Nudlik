from abc import ABC, abstractmethod
from dataclasses import dataclass

import PIL
from PIL.Image import Image


@dataclass
class ImageInterface(ABC):
    open_provider: None


@dataclass
class ImageAdapter(ImageInterface, Image):
    open_provider: PIL.Image.open
