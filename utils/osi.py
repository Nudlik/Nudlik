import os as os_default
from abc import abstractmethod, ABC
from dataclasses import dataclass


@dataclass(eq=False)
class OSInterface(ABC):
    os: None


@dataclass(eq=False)
class OSI(OSInterface):
    os: os_default
