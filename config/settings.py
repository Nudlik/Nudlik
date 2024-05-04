# данные для парсинга
PARS_DATA = [
    {
        'url': 'https://stepik.org/users/564742454/',
        'file_name': 'stepik_stats.png',
        'tag': '.cal-heatmap-container',
        'coords_local': (391, 189, 1146, 451),
        'coords_remote': (398, 189, 1152, 451)
    },
    {
        'url': 'https://codeium.com/profile/nudlik',
        'file_name': 'codeium_stats.png',
        'tag': 'body',
        'coords_local': (430, 430, 1101, 560),
        'coords_remote': (457, 426, 1164, 560),
    }
]

# настройки браузера и папок для сейва
WEB_BROWSER_NAME = 'Firefox'
IMG_DIR = 'img'

# выбираем по каким координатам будет обрезать скриншот
REMOTE = False