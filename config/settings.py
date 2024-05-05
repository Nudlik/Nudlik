# данные для парсинга
PARS_DATA = [
    {
        'url': 'https://stepik.org/users/564742454/',
        'file_name': 'stepik_stats.png',
        'tag': '.cal-heatmap-container',
        'coords_local': (391, 189, 1146, 451),
        'coords_remote': (382, 190, 1138, 451)
    },
    {
        'url': 'https://codeium.com/profile/nudlik',
        'file_name': 'codeium_stats.png',
        'tag': 'body',
        'coords_local': (430, 430, 1101, 560),
        'coords_remote': (425, 427, 1090, 555),
    }
]

# настройки браузера и папок для сейва
WEB_BROWSER_NAME = 'Firefox'
WEB_BROWSER_WINDOW_SIZE = (1280, 1000)
IMG_DIR = 'img'

# выбираем по каким координатам будет обрезать скриншот
REMOTE = True
