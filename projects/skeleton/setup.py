try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Pinpin',
    'url': 'https://github.com/nipsalvin/lpthw',
    'download_url': 'https://github.com/nipsalvin/lpthw',
    'author_email': 'My email',
    'version': '0.1',
    'install_requirements': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)