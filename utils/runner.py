from abc import abstractmethod, ABC
from dataclasses import dataclass

from utils.images import ImageInterface, Images
from utils.osi import OSInterface, OSI
from utils.screenshot import ScreenShotInterface, ScreenShot


@dataclass(eq=False)
class RunnerInterface(ABC):
    screenshot_interface: ScreenShotInterface
    image_interface: ImageInterface
    os_interface: OSInterface

    @abstractmethod
    def run(self):
        pass


@dataclass(eq=False)
class Runner(RunnerInterface):
    screenshot_interface: ScreenShot
    image_interface: Images
    os_interface: OSI

    def run(self):
        pass

    def download_screenshots(self, browser_name, folder_img, data):
        with self.screenshot_interface as browser:
            for item in data:
                browser.make_screenshot(item['url'], item['file_name'], item['tag'])

    def refactor_screenshots(self, folder_img, data):
        for item in data:
            path = self.os_interface.os.path.join(folder_img, item['file_name'])
            with self.image_interface.open_provider(path) as img:
                with img.crop(item['coords_local']) as cropped_img:
                    cropped_img.save(self.os_interface.os.path.join(folder_img, 'result_' + item['file_name']))
