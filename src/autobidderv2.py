from src.config import URL
from src.config import create_driver, USER
from src.helpers import *

from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
import xlwt
from xlwt import Workbook
import openpyxl
import os
from datetime import datetime
from datetime import date
from time import sleep
import random

class Autobidderv2:
    def __init__(self, driver):

        # Notice how the webdriver is passed into this function
        self.driver = driver
        self.num_watchlist = 0
        self.num_transferlist = 0

        self.number_of_bids = 0
        self.bids_available = 0

        self.sellprice = 0
        self.playername = ""
        self.max_price = 0

        self.num_increases = 0

        self.players_futbin_prices = []

    def testfunc(self, driver, playerdata):
        print("Autobidderv2 line 42. TEST FUNCTION! It should open a new tab and look up the first player in the list. You  can change this message and hit Reload Functions to see how the function updates")
        self.futbinscraper(playerdata)

    def printplayerlist(self, driver, playerdata):
        print("Player list: ")
        print(playerdata)
        print("Add a new player and reload the functions, and see it updated")

    def login(self, userinfo):
        print("This function should log you in ")

    def futbinscraper(self, playerdata):
        player1name = playerdata[0][1]
        tab_url = "https://www.google.com/search?q=" + str(player1name)

        browser = self.driver

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get(tab_url)
        print("Current Page Title is : %s" %browser.title)
        print("Sleeping for 15 secs and then closing the tab")
        # ~ ~ ~ ~ ~ ~ Do Stuff in new tab here ~ ~ ~ ~ ~
        sleep(15)
        # ~ ~ ~ ~ ~ ~ ~ Close the futbin tab ~ ~ ~ ~ ~
        browser.close()

        # Switch back to the first tab with URL A
        browser.switch_to.window(browser.window_handles[0])
        print("Current Page Title is : %s" %browser.title)
