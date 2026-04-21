import scrapy
import mysql.connector

class GetMovieDetailsSpiderSpider(scrapy.Spider):
    name = "get_movie_details_spider"
    # allowed_domains = ["www.rottentomatoes.com"]
    # start_urls = ["https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest"]




import scrapy
import json
import mysql.connector

base_url = "https://www.rottentomatoes.com"


class GetMovieDetailsSpiderSpider(scrapy.Spider):
    name = "get_movie_details_spider"

    # ---------- HEADERS ----------
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'akamai_generated_location={"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=82~id=118cab4333c61f05ea6abe27ceec9ef8; eXr91Jra=Az_yh6mdAQAAwf-PxK41aLz5o6LdcENLztJCK_4GFDlGXYUzqXNu3f1DoI0FAcI9KGCuco1HwH8AAEB3AAAAAA|1|0|bf1a09417dd1127b19bb88d3c28fbc3d3f4fb798; usprivacy=1---; OptanonAlertBoxClosed=2026-04-20T06:15:58.476Z; OneTrustWPCCPAGoogleOptOut=false; _ALGOLIA=anonymous-f4663f31-439d-4ae4-aaae-c028891a72d6; _cb=B2QkZ8BdmX6RBGx3nJ; check=true; algoliaUT=6a5dfa36-01f2-421a-975a-4763025bed99; __host_color_scheme=JteVcojf-1dA6QJhXuLkYossARKNVIPi4HiMhdP6Ld9NxmgKa8TM; __host_theme_options=1776666313156; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C15553540245624872380013280458890593436%7CMCAAMLH-1777282425%7C12%7CMCAAMB-1777282425%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776684825s%7CNONE%7CvVersion%7C4.6.0%7CMCIDTS%7C20564; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+15%3A43%3A21+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=a0702456-efc5-46e1-ac26-eecf2dce2da0&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&crTime=1776665759917&geolocation=SG%3B&AwaitingReconsent=false; mbox=PC#d80507713c534d2ea8f4d09437c8b852.41_0#1839910558|session#ee78503a6b154df5b3f4fc2ee650b634#1776681864; sailthru_pageviews=3; _chartbeat2=.1776665760185.1776680005100.1.BkLgvIQ3oAIBTbFsEBVorI911nEn.1; _cb_svref=external; _awl=2.1776680006.5-2063d19ecc891d1de23bfe2ef967bcf3-6763652d617369612d6561737431-0; __gads=ID=71e4721fefb9c8b3:T=1776665761:RT=1776680006:S=ALNI_MZWiouZQt_99XIH-B4gt0yN9fTaxA; __gpi=UID=0000126e16a0641c:T=1776665761:RT=1776680006:S=ALNI_MbQiWyRqlyBbRkqtA5nBDs8jbguOg; __eoi=ID=05032d3e4192e565:T=1776665761:RT=1776680006:S=AA-AfjaFa8qfKuX7L06bjXXUjHFN; QSI_HistorySession=https%3A%2F%2Fwww.rottentomatoes.com%2Fm%2Fover_your_dead_body_2026~1776680006506; cto_bundle=3-A7k19NaGx4bWRRVXNrQnZ2aHVoRlZoeDJ2UUhDMEZsWGIxYlVMUFIlMkJDbXBVOGdYMVlXcHRIJTJGS3lxVjdHb0NZQU1HQUElMkJnTWRRRmIyNCUyQktpN2d5ZUU0YVNSMkp2eU5zalRjOGZ4Y1BpbGJ3TUR6Z1F3WDFQcm5aZFU3a2Zlb0tudHlxaFhRZlZQY0JMSG9LN09hMEhqb1B4TGJ0UE1sbiUyQmQlMkZMWTlrdGJuc2h4NUElM0Q',
    }

    api_headers = {
        "user-agent": "Mozilla/5.0",
        "accept": "application/json",
    }

    # ---------- COOKIES ----------
    cookies = {
        'akamai_generated_location': '{"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}',
        'akacd_RTReplatform': '2147483647~rv=82~id=118cab4333c61f05ea6abe27ceec9ef8',
        'eXr91Jra': 'Az_yh6mdAQAAwf-PxK41aLz5o6LdcENLztJCK_4GFDlGXYUzqXNu3f1DoI0FAcI9KGCuco1HwH8AAEB3AAAAAA|1|0|bf1a09417dd1127b19bb88d3c28fbc3d3f4fb798',
        'usprivacy': '1---',
        'OptanonAlertBoxClosed': '2026-04-20T06:15:58.476Z',
        'OneTrustWPCCPAGoogleOptOut': 'false',
        '_ALGOLIA': 'anonymous-f4663f31-439d-4ae4-aaae-c028891a72d6',
        '_cb': 'B2QkZ8BdmX6RBGx3nJ',
        'check': 'true',
        'algoliaUT': '6a5dfa36-01f2-421a-975a-4763025bed99',
        '__host_color_scheme': 'JteVcojf-1dA6QJhXuLkYossARKNVIPi4HiMhdP6Ld9NxmgKa8TM',
        '__host_theme_options': '1776666313156',
        'AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg': '1',
        's_cc': 'true',
        's_sq': '%5B%5BB%5D%5D',
        'AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg': '-408604571%7CMCMID%7C15553540245624872380013280458890593436%7CMCAAMLH-1777282425%7C12%7CMCAAMB-1777282425%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776684825s%7CNONE%7CvVersion%7C4.6.0%7CMCIDTS%7C20564',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+20+2026+15%3A43%3A21+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=a0702456-efc5-46e1-ac26-eecf2dce2da0&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&crTime=1776665759917&geolocation=SG%3B&AwaitingReconsent=false',
        'mbox': 'PC#d80507713c534d2ea8f4d09437c8b852.41_0#1839910558|session#ee78503a6b154df5b3f4fc2ee650b634#1776681864',
        'sailthru_pageviews': '3',
        '_chartbeat2': '.1776665760185.1776680005100.1.BkLgvIQ3oAIBTbFsEBVorI911nEn.1',
        '_cb_svref': 'external',
        '_awl': '2.1776680006.5-2063d19ecc891d1de23bfe2ef967bcf3-6763652d617369612d6561737431-0',
        '__gads': 'ID=71e4721fefb9c8b3:T=1776665761:RT=1776680006:S=ALNI_MZWiouZQt_99XIH-B4gt0yN9fTaxA',
        '__gpi': 'UID=0000126e16a0641c:T=1776665761:RT=1776680006:S=ALNI_MbQiWyRqlyBbRkqtA5nBDs8jbguOg',
        '__eoi': 'ID=05032d3e4192e565:T=1776665761:RT=1776680006:S=AA-AfjaFa8qfKuX7L06bjXXUjHFN',
        'QSI_HistorySession': 'https%3A%2F%2Fwww.rottentomatoes.com%2Fm%2Fover_your_dead_body_2026~1776680006506',
        'cto_bundle': '3-A7k19NaGx4bWRRVXNrQnZ2aHVoRlZoeDJ2UUhDMEZsWGIxYlVMUFIlMkJDbXBVOGdYMVlXcHRIJTJGS3lxVjdHb0NZQU1HQUElMkJnTWRRRmIyNCUyQktpN2d5ZUU0YVNSMkp2eU5zalRjOGZ4Y1BpbGJ3TUR6Z1F3WDFQcm5aZFU3a2Zlb0tudHlxaFhRZlZQY0JMSG9LN09hMEhqb1B4TGJ0UE1sbiUyQmQlMkZMWTlrdGJuc2h4NUElM0Q',
    }

    # error handling
    def handle_http_error(self, failure):
            request = failure.request

            url = request.url
            category_name = request.meta.get("category_name")

            # Detect error type
            error_type = type(failure.value).__name__

            self.logger.error(
                f"HTTP ERROR: {url} | TYPE: {error_type}"
            )

    # ---------- DB ----------
    def fetch_all_movies(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="actowiz",
            database="rotten_tomatoes_scrapy_db"
        )

        cursor = connection.cursor(dictionary=True)
        # cursor.execute("SELECT * FROM movie_urls WHERE id=12")

        cursor.execute("SELECT * FROM movie_urls WHERE status='pending'")
        rows = cursor.fetchall()

        cursor.close()
        connection.close()
        return rows

    def update_status(self, movie_id, status):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="actowiz",
            database="rotten_tomatoes_scrapy_db"
        )
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE movie_urls SET status=%s WHERE id=%s",
            (status, movie_id)
        )
        connection.commit()
        cursor.close()
        connection.close()

    # ---------- START ----------
    def start_requests(self):
        rows = self.fetch_all_movies()

        for row in rows:
            yield scrapy.Request(
                url=row["movie_url"],
                headers=self.headers,
                cookies=self.cookies,
                callback=self.parse_movie,
                meta={"row": row},
                dont_filter=True
            )
            # break

    # ---------- STEP 1: MOVIE PAGE ----------
    def parse_movie(self, response):
        row = response.meta["row"]

        script = response.xpath("//script[@data-json='mediaScorecard']/text()").get()
        data = json.loads(script) if script else {}

        movie_id = data.get("criticReviewHref", "").split("/movie/")[-1]

        item = {
            "movie_name": row["movie_name"],
            "movie_url": row["movie_url"],
            "description": data.get("description"),
            "image_url": data.get("primaryImageUrl"),
            "reviews": data.get("overlay", {}).get("criticsAll", {}).get("scoreLinkText"),
            "scorePercent": data.get("criticsScore", {}).get("scorePercent"),
            "movie_id": movie_id,
            "row_id": row["id"]
        }


        # #  next: cast page
        yield scrapy.Request(
            url=row["movie_url"] + "/cast-and-crew",
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse_cast,
            meta={"item": item},
            dont_filter=True
        )

    # ---------- STEP 2: CAST ----------
    def parse_cast(self, response):
        item = response.meta["item"]

        cast_list = []

        cards = response.xpath("//cast-and-crew-card")

        for card in cards:
            cast_list.append({
                "cast_name": card.xpath(".//rt-text[@slot='title']/text()").get(),
                "characters": card.xpath(".//rt-text[@slot='characters']/text()").get(),
                "credits": card.xpath(".//rt-text[@slot='credits']/text()").get(),
                "cast_url": base_url + (card.xpath("./@media-url").get() or ""),
                "cast_image_url": card.xpath(".//rt-img/@src").get()
            })

        item["cast_and_crew"] = cast_list
        # print("-------cast_and_crew------", item)


        review_headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f"{item['movie_url']}/reviews",
            'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        }

        params = "after=&before=&pageCount=20&topOnly=false&type=critic&verified=false"

        url = f"https://www.rottentomatoes.com/napi/rtcf/v1/movies/{item['movie_id']}/reviews?{params}"

        yield scrapy.Request(
            url=url,
            headers=review_headers,
            callback=self.parse_reviews,
            meta={"item": item},
            dont_filter=True
        )

    # ---------- STEP 3: REVIEWS ----------
    def parse_reviews(self, response):
        item = response.meta["item"]

        data = json.loads(response.text)
        review_list = []

        for r in data.get("reviews", []):
            review_list.append({
                "name": r.get("critic", {}).get("displayName"),
                "review_type": r.get("scoreSentiment"),
                "reviewQuote": (r.get("reviewQuote") or "").replace("&#44;", ","),
                "language": r.get("language"),
            })

        item["reviews_data"] = review_list
        # print("-------reviews_data------", item)



        #  next: videos page
        yield scrapy.Request(
            url=item["movie_url"] + "/videos",
            headers=self.headers,
            cookies=self.cookies,
            callback=self.parse_videos,
            errback=self.handle_http_error,
            meta={"item": item, "handle_httpstatus_all": True},
            dont_filter=True
        )

    # ---------- STEP 4: VIDEOS ----------
    def parse_videos(self, response):
        item = response.meta["item"]

        if response.status != 200:
            self.logger.error(f"BAD STATUS {response.status}: {response.url}")
            # self.update_category_status("pending", category_id)
            yield {
                "type" : "movie_details",
                "movie_name" : item["movie_name"],
                "movie_url" : item["movie_url"],
                "description" : item["description"],
                "image_url" : item["image_url"],
                "reviews" : item["reviews"],
                "scorePercent" : item["scorePercent"],
                "cast_and_crew" : json.dumps(item["cast_and_crew"]),
                "review_data_details" : json.dumps(item["reviews_data"]),
                "video_url" : json.dumps([])
            }
            # update DB AFTER success
            self.update_status(item["row_id"], "success")

            return


        script = response.xpath("//script[@type='application/json']/text()").get()
        data = json.loads(script) if script else []

        videos = []
        for v in data:
            videos.append({
                "video_title": v.get("title"),
                "video_url": base_url + v.get("videoPageUrl", "")
            })

        item["videos"] = videos

        # print("-------parse_videos------", item)

        yield {
            "type" : "movie_details",
            "movie_name" : item["movie_name"],
            "movie_url" : item["movie_url"],
            "description" : item["description"],
            "image_url" : item["image_url"],
            "reviews" : item["reviews"],
            "scorePercent" : item["scorePercent"],
            "cast_and_crew" : json.dumps(item["cast_and_crew"]),
            "review_data_details" : json.dumps(item["reviews_data"]),
            "video_url" : json.dumps(item["videos"])
        }
        # update DB AFTER success
        self.update_status(item["row_id"], "success")







