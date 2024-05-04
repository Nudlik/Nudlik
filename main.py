import os

import PIL

from config.settings import PARS_DATA, WEB_BROWSER_NAME, IMG_DIR
from utils.imageadapter import ImageAdapter
from utils.osadapter import OSAdapter
from utils.runner import Runner
from utils.screenshot import ScreenShot


def main() -> None:
    runner = Runner(
        screenshot_interface=ScreenShot(
            browser_name=WEB_BROWSER_NAME,
            screen_root_dir=IMG_DIR
        ),
        image_interface=ImageAdapter(
            open_provider=PIL.Image.open
        ),
        os_interface=OSAdapter(
            os=os,
            folder_img=IMG_DIR,
            prefix_result_img='result_',
        ),
        data=PARS_DATA,
    )
    runner.run()


if __name__ == '__main__':
    main()
