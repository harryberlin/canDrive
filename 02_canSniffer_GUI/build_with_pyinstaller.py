#  -*- coding: utf-8 -*-

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '-ican-bus.png',

])
