try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Martin Hora',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'martin.hora11@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['scrabble'],
    'scripts': [],
    'name': 'Scrabble Cheat'
}

setup(**config)
