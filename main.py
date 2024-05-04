import os

import PIL

from config.settings import PARS_DATA, WEB_BROWSER_NAME, IMG_DIR, REMOTE
from utils.imageadapter import ImageAdapter
from utils.osadapter import OSAdapter
from utils.runner import Runner
from utils.screenshot import ScreenShot


def main() -> None:
    """ Точка входа в программу """

    screenshot_interface = ScreenShot(
        browser_name=WEB_BROWSER_NAME,
        window_size=(1280, 1000),
    )
    image_interface = ImageAdapter(
        open_provider=PIL.Image.open,
    )
    os_interface = OSAdapter(
        os=os,
        folder_img=IMG_DIR,
        prefix_result_img='result_',
    )
    runner = Runner(
        screenshot_interface=screenshot_interface,
        image_interface=image_interface,
        os_interface=os_interface,
        data=PARS_DATA,
        REMOTE=REMOTE,
    )
    runner.run()


if __name__ == '__main__':
    main()
