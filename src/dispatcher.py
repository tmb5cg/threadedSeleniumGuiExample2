import src.autobidderv2
import src.helpers

from src.autobidderv2 import *
from src.helpers import *

from src.config import USER

# I think they need to be imported in the above format here too, I can't remember
import threading


# Each button starts a new thread
class Dispatcher(threading.Thread):
    def __init__(self, queue, driver, action, searchdata):
        threading.Thread.__init__(self)
        self.action = action
        self.queue = queue
        self.searchdata = searchdata
        self.driver = driver

        self.autobidderv2 = Autobidderv2(self.driver)

        self.pricedata = ""

    def run(self):

        # Add actual functions here
        if self.action == "test":
            self.queue.put("Test button")
            self.autobidderv2.testfunc(self.driver, self.searchdata)

        if self.action == "print player list":
            self.queue.put("Printing player list, line 34 in dispatcher. will now call function in autobidderv2.py. Notice that I pass the driver element to the method, it is also passed to the autobidder object in line 22. so this isn't really necessary")
            self.autobidderv2.printplayerlist(self.driver, self.searchdata)

        if self.action == "futbin scraper":
            self.queue.put("Futbin Scraping")
            self.autobidderv2.futbinscraper(self.searchdata)
