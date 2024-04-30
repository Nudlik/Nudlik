import os.path

from utils.screenshot import ScreenShot
from PIL import Image

PARS_DATA = [
    {
        'url': 'https://stepik.org/users/564742454/',
        'file_name': 'stepik_stats.png',
        'tag': '.cal-heatmap-container',
        'coords': (398, 189, 1152, 451)
    },
    {
        'url': 'https://codeium.com/profile/nudlik',
        'file_name': 'codeium_stats.png',
        'tag': 'body',
        'coords': (457, 434, 1164, 560)
    }
]


def download_screenshots(browser_name, folder_img, data):
    with ScreenShot(browser_name, folder_img) as browser:
        for item in data:
            browser.make_screenshot(item['url'], item['file_name'], item['tag'])


def refactor_screenshots(folder_img, data):
    for item in data:
        path = os.path.join(folder_img, item['file_name'])
        img = Image.open(path)
        cropped_img = img.crop(item['coords'])
        cropped_img.save(os.path.join(folder_img, 'result_' + item['file_name']))
        img.close()
        cropped_img.close()


if __name__ == '__main__':
    web_browser_name = 'firefox'
    root_img_dir = 'img'
    download_screenshots(web_browser_name, root_img_dir, PARS_DATA)
    refactor_screenshots(root_img_dir, PARS_DATA)
