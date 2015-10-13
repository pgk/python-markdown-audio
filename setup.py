from distutils.core import setup
from mdx_video import __version__, __author__

setup(name='mdx_audio',
      version=__version__,
      description='Markdown 2.0 extension for embedding audio files',
      author=__author__,
      author_email='panosktn@gmail.com',
      url='https://github.com/pgk/python-markdown-soundmanager2',
      py_modules = ['mdx_audio'],
)
