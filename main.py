import os

import PIL

from config.settings import PARS_DATA
from utils.images import Images
from utils.osi import OSI
from utils.runner import Runner
from utils.screenshot import ScreenShot


def main() -> None:
    web_browser_name = 'Firefox'
    root_img_dir = 'img'
    runner = Runner(
        screenshot_interface=ScreenShot(web_browser_name, root_img_dir),
        image_interface=Images(open_provider=PIL.Image.open),
        os_interface=OSI(os),
    )
    runner.download_screenshots(web_browser_name, root_img_dir, PARS_DATA)
    runner.refactor_screenshots(root_img_dir, PARS_DATA)


if __name__ == '__main__':
    main()
