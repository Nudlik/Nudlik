from utils.screenshot import ScreenShot

PARS_DATA = [
    {
        'url': 'https://stepik.org/users/564742454/',
        'file_name': 'stepik_stats.png',
        'tag': '.cal-heatmap-container'
    },
    {
        'url': 'https://codeium.com/profile/nudlik',
        'file_name': 'codeium_stats.png',
        'tag': 'body'
    }
]


def download_screenshots(browser_name, data):
    with ScreenShot(browser_name, 'img') as browser:
        for item in data:
            browser.make_screenshot(item['url'], item['file_name'], item['tag'])


def refactor_screenshots():
    pass


if __name__ == '__main__':
    web_browser_name = 'firefox'
    download_screenshots(web_browser_name, PARS_DATA)
