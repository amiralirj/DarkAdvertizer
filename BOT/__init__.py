import sys
import os
SCRIPT_DIR = str(os.path.dirname(os.path.abspath(__file__))).strip(r'\plugins\BOT')
sys.path.insert(-1,(SCRIPT_DIR))
CWD=os.getcwd()
del os , sys
from Advertiserbot import Advertising , Rj
import  Config
from Config import TEXTS , BUTTONS 
from Classes.NumberClass import Number
from Classes.UserClass import User
RJ=Rj()