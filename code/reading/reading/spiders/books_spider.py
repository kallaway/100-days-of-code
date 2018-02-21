import scrapy


class BooksSpider(scrapy.Spider):
  name = "books"
  start_urls = [
    'https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once',
  ]

  def parse(self, response):
    for book_title in response.css('#all_votes table td a.bookTitle::attr(href)'):




  #all_votes table tbody tr td  a


