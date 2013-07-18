from akorn.scrapers.base import BaseScraper

from datetime import datetime
import time

class Scraper(BaseScraper):
    # List of domains that scraper is for
    domains = ['prl.aps.org', 'prx.aps.org']
    # Relative name of config file
    config = 'simons.xml'

 
