import os

import PIL

from config.settings import PARS_DATA, WEB_BROWSER_NAME, IMG_DIR, REMOTE, WEB_BROWSER_WINDOW_SIZE
from utils.imageadapter import ImageAdapter
from utils.osadapter import OSAdapter
from utils.runner import Runner
from utils.screenshot import ScreenShot


def main() -> None:
    """ Точка входа в программу """

    screenshot_service = ScreenShot(
        browser_name=WEB_BROWSER_NAME,
        window_size=WEB_BROWSER_WINDOW_SIZE,
    )
    image_service = ImageAdapter(
        open_provider=PIL.Image.open,
    )
    os_service = OSAdapter(
        os=os,
        folder_img=IMG_DIR,
        prefix_result_img='result_',
    )
    runner = Runner(
        screenshot_service=screenshot_service,
        image_service=image_service,
        os_service=os_service,
        data=PARS_DATA,
        REMOTE=REMOTE,
    )
    runner.run()


if __name__ == '__main__':
    main()
