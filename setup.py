try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'mplookup',
        'auhtor': 'Chris Nicholas',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'nchris27@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['mplookup'],
        'scripts': ['mpscript.py'],
        'name': 'mplookup'
}

setup(**config)
