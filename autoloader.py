from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import scrolledtext
from pytube import Playlist
from pytube import YouTube

import time,random,threading


from data.store import Store
from data.schema import Schema
from core.FileInterface import FileInterface
from core.argparse import ArgsParse
from view.FileMenu import FileMenu
from view.EditMenu import EditMenu
from view.HelpMenu import HelpMenu
from view.PageMenu import PageMenu
from view.baseTheme import BaseTheme
from view.videoInfo import VideoInfo
from view.tab import TabContronller

from view.index import Index
from core.jsonparser import JsonParser
from controllers.search import Search