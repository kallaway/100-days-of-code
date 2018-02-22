import scrapy
from urllib.parse import urljoin
from cucco import Cucco
import logging
logger = logging.getLogger(__name__)

class BooksSpider(scrapy.Spider):
  name = "books"
  root_domain = 'https://www.goodreads.com'
  start_urls = [
    'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once',
  ]

  @classmethod
  def clean_string(cls, s):
    try:
      assert (isinstance(s, str) and len(s) > 0), 'The string is invalid'
      cucco = Cucco()
      normalizations = [
        'remove_extra_white_spaces',
        'remove_accent_marks',
        ('replace_symbol', {'replacement': '_'}),
        ('replace_emojis', {'replacement': ''}),
        ('replace_urls', {'replacement': ''}),
      ]
      if s[0].isdigit():
        s = 'x{}'.format(s)
      new_s = cucco.normalize(s, normalizations).lower().rstrip('-_')
      return True, new_s
    except AssertionError as e:
      logger.exception(str(e))
      return False, None
    except Exception as e:
      logger.exception('Error while cleaning string {}'.format(str(e)))
      return False, None

  def parse(self, response):
    book_page_urls = response.css('#all_votes table td a.bookTitle::attr(href)').extract()
    next_page_urls = response.css('div.pagination a.next_page::attr(href)').extract()
    book_title = response.css('h1#bookTitle.bookTitle::text').extract_first()
    book_rating = response.css('span.rating span.average::text').extract_first()
    num_ratings = response.css('#bookMeta a span.votes.value-title::text').extract_first()
    num_review = response.css('#bookMeta a span.count.value-title::text').extract_first()
    num_pages = response.css('#details div span:nth-child(2)::text').extract_first()

    if book_title:
      #create a dictionary to store the scraped info
      scraped_info = {
          'title' : self.clean_string(book_title)[1],
          'rating' : book_rating,
          'url' : response.url
      }
      yield scraped_info


    for url in book_page_urls + next_page_urls:
      book_page_url = urljoin(self.root_domain, url)
      yield scrapy.Request(book_page_url, callback=self.parse)




