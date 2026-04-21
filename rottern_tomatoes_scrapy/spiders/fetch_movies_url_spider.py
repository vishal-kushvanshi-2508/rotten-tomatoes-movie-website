from urllib.parse import urlencode

import scrapy
import json
from urllib.parse import urlencode



class FetchMoviesUrlSpiderSpider(scrapy.Spider):
    name = "fetch_movies_url_spider"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest"]

    def parse(self, response):
        self.logger.info("---------parse-----------")

        # Extract pageInfo (for pagination cursor)
        next_page = response.xpath("//script[@id='pageInfo']/text()").get()
        next_page_id = None

        if next_page:
            next_page_data = json.loads(next_page)
            next_page_id = next_page_data.get("endCursor")

        # Extract movies from ld+json
        script_data = response.xpath(
            "//script[@type='application/ld+json']/text()"
        ).get()

        if script_data:
            python_dict = json.loads(script_data)

            item_list = python_dict.get("itemListElement", {}).get(
                "itemListElement", []
            )

            for movie in item_list:
                yield {
                    "type" : "all_movie_url",
                    "movie_name": movie.get("name"),
                    "movie_url": movie.get("url"),
                    "status": "pending",
                }

        params = {'after': next_page_id}
        url = "https://www.rottentomatoes.com/cnapi/browse/movies_in_theaters/sort:newest?" + urlencode(params)
        
        # Call pagination API if cursor exists
        if next_page_id:
            yield scrapy.Request(
                url=url,
                callback=self.parse_pagination,
                meta={"cursor": next_page_id},
                dont_filter=True
            )

    def parse_pagination(self, response):
        cursor = response.meta.get("cursor")

        data = json.loads(response.text)

        movie_list = data.get("grid", {}).get("list", [])

        if not movie_list:
            return

        # Extract movies
        for movie in movie_list:
            yield {
                "type" : "all_movie_url",
                "movie_name": movie.get("title"),
                "movie_url": "https://www.rottentomatoes.com" + movie.get("mediaUrl"),
                "status": "pending",
            }

        # Get next cursor
        next_cursor = data.get("pageInfo", {}).get("endCursor")

        if next_cursor:
            yield scrapy.Request(
                url=f"https://www.rottentomatoes.com/cnapi/browse/movies_in_theaters/sort:newest?after={next_cursor}",
                callback=self.parse_pagination,
                meta={"cursor": next_cursor},
                dont_filter=True
            )