import os

import PIL

from config.settings import PARS_DATA, WEB_BROWSER_NAME, IMG_DIR, REMOTE
from utils.imageadapter import ImageAdapter
from utils.osadapter import OSAdapter
from utils.runner import Runner
from utils.screenshot import ScreenShot


def main() -> None:
    """ Точка входа в программу """

    screenshot_interface = ScreenShot(WEB_BROWSER_NAME)
    image_interface = ImageAdapter(PIL.Image.open)
    os_interface = OSAdapter(os, IMG_DIR, 'result_')

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
