import akorn.scrapers.journals.scrape_meta_tags as s

from akorn.scrapers.journals.comm import *
from akorn.scrapers.journals.utils import *

#Current Journals:
#Proceedings of the Royal Society A & B


SCRAPER_DOMAINS = ['rspb.royalsocietypublishing.org',
                   'rspa.royalsocietypublishing.org']



def scrape(abstract_url):

    tree, urls, page_text = get_tree(abstract_url) 

    article = s.scrape_tree(tree, urls, page_text)

    #For P.R.C:A and P.R.C:B
    if article['journal'] == 'Proceedings of the Royal Society A: \
Mathematical, Physical and Engineering Science' or\
    article['journal'] == 'Proceedings of the Royal Society B: \
Biological Sciences':

        article['abstract'] = tree.xpath("//div[@class='section abstract']/p")[0].text_content()


    return article




    
