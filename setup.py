from distutils.core import setup
from hulu_subs_dl import __version__

readme = open('ReadMe.md').read()
history = open('Changelog.md').read()

setup(
    name='hulusubs_dl',
    packages=['hulu_subs_dl', 'hulu_subs_dl.api', 'hulu_subs_dl.cust_utils'],  # this must be the same as the name above
    install_requires=["requests"],
    version=__version__,
    description='hulusubs_dl is a command line tool to download subtitles from ',
    long_description=readme + '\n\n' + history,
    author='Xonshiz',
    author_email='xonshiz@gmail.com',
    url='https://github.com/Xonshiz/Hulu-Subs-Downloader',
    download_url='https://github.com/Xonshiz/Hulu-Subs-Downloader/releases/latest',
    keywords=['hulusubs_dl', 'cli', 'subtitle downloader', 'hulu subtitle downloader', 'hulu'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent'
    ],
)
