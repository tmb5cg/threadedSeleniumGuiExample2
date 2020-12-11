from src.config import USER
from src.config import URL
from src.config import create_driver



import random
from time import sleep
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from datetime import datetime
import xlwt
from xlwt import Workbook
import openpyxl
import os
import logging
import threading
import time
import queue
from datetime import date
import json
from lxml import html
import requests
from pprint import pprint
from csv import reader

def wait_for_shield_invisibility(driver, duration=0.25):
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, 'ut-click-shield showing interaction'))
    )
    sleep(duration)
