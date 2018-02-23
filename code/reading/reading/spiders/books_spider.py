import scrapy
from urllib.parse import urljoin
from cucco import Cucco
import logging
import numpy as np
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
      new_s = cucco.normalize(s, normalizations).lower().rstrip('-_')
      return True, new_s
    except AssertionError as e:
      logger.exception(str(e))
      return False, None
    except Exception as e:
      logger.exception('Error while cleaning string {}'.format(str(e)))
      return False, None

  @classmethod
  def get_top_3_genres(cls, genres, genres_users):
    try:
      genres = [cls.clean_string(x)[1] for x in genres if cls.clean_string(x)[0]]
      genre_users = [cls.clean_string(x)[1] for x in genres_users if cls.clean_string(x)[0]]
      get_digits = lambda y: list(filter(lambda x: x.replace(',','').isdigit(), y.split()))[0]
      genres_scores_map = map(lambda x: int(get_digits(x).replace(',', '')) , genre_users)
      genres_scores = np.fromiter(genres_scores_map, dtype=np.float)
      genres_weights = genres_scores / genres_scores.sum()
      genres_with_weights = sorted(list(zip(genres_weights, genres)), key=lambda x: x[0], reverse=True)
      return [genre for _, genre in genres_with_weights[:3]]
    except Exception as e:
      return []


  def parse(self, response):
    book_page_urls = response.css('#all_votes table td a.bookTitle::attr(href)').extract()
    next_page_urls = response.css('div.pagination a.next_page::attr(href)').extract()
    book_title = response.css('h1#bookTitle.bookTitle::text').extract_first()
    book_rating = response.css('span.rating span.average::text').extract_first()
    num_ratings = response.css('#bookMeta a span.votes.value-title::text').extract_first()
    num_review = response.css('#bookMeta a span.count.value-title::text').extract_first()
    num_pages = response.css('#details div span:nth-child(2)::text').extract_first()
    genres = response.css('div.left a.bookPageGenreLink:nth-child(1)::text').extract()
    genre_users = response.css('div.right a.bookPageGenreLink::text').extract()
    top_genres = self.get_top_5_genres(genres, genre_users)

    if book_title:
      #create a dictionary to store the scraped info
      scraped_info = {
          'title' : self.clean_string(book_title)[1],
          'rating' : book_rating,
          'url' : response.url,
          'genres' : top_genres,
          'num_ratings' : num_ratings,
          'num_review' : num_review,
          'num_pages' : num_pages
      }
      yield scraped_info

    for url in book_page_urls + next_page_urls:
      book_page_url = urljoin(self.root_domain, url)
      yield scrapy.Request(book_page_url, callback=self.parse)




