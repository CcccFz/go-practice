try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
	'author_email': 'ccccfz@163.com',
	'url': 'URL to get it all',
	'download_url': 'where to download it',
	'version': '0.1',
	'scripts': [],
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'name': 'projectname'
}

setup(**config)