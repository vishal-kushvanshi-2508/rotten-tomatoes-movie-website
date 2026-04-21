import requests
from lxml import html
import json

from store_data_database import *
 
base_url = "https://www.rottentomatoes.com"

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


review_cookies = {
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
    '_cb_svref': 'external',
    'AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg': '-408604571%7CMCMID%7C15553540245624872380013280458890593436%7CMCAAMLH-1777289958%7C12%7CMCAAMB-1777289958%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776692358s%7CNONE%7CvVersion%7C4.6.0%7CMCIDTS%7C20564',
    's_sq': '%5B%5BB%5D%5D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+20+2026+17%3A16%3A39+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=a0702456-efc5-46e1-ac26-eecf2dce2da0&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&crTime=1776665759917&geolocation=SG%3B&AwaitingReconsent=false',
    'sailthru_pageviews': '19',
    'mbox': 'PC#d80507713c534d2ea8f4d09437c8b852.41_0#1839910558|session#ee78503a6b154df5b3f4fc2ee650b634#1776687460',
    '_chartbeat2': '.1776665760185.1776685600276.1.CQJ11gCcP6qXCux0BRBUmVv_DRaZik.4',
    '_awl': '2.1776685601.5-2063d19ecc891d1de23bfe2ef967bcf3-6763652d617369612d6561737431-0',
    '__gads': 'ID=71e4721fefb9c8b3:T=1776665761:RT=1776685602:S=ALNI_MZWiouZQt_99XIH-B4gt0yN9fTaxA',
    '__gpi': 'UID=0000126e16a0641c:T=1776665761:RT=1776685602:S=ALNI_MbQiWyRqlyBbRkqtA5nBDs8jbguOg',
    '__eoi': 'ID=05032d3e4192e565:T=1776665761:RT=1776685602:S=AA-AfjaFa8qfKuX7L06bjXXUjHFN',
    'cto_bundle': 'UDBiB19NaGx4bWRRVXNrQnZ2aHVoRlZoeDJ0bURvS2dsa21tS3YyaSUyQm9Eb0FLcnowU3JieFZoaUhUdXVlNUtVNnF2Mm51RnVBems0Vm1LJTJGUm9POE15Rnl1N2hPamo0dXdQdERaaWtUQmFEemlSaTZqWWhWVUtPalpLRVhyZFlPb0V4cm43NSUyRnI5MXUlMkJsTCUyRkRnT3Z0V3RkJTJGdXNDZmdIYmpQZkhrdE0lMkZvU2REYk8lMkZBJTNE',
    '_chartbeat4': 't=BLiyF_DjOOx4BhK67VDQb02BwRowo&E=6&x=333&c=0.41&y=5281&w=346',
}

review_params = {
    'after': '',
    'before': '',
    'pageCount': '20',
    'topOnly': 'false',
    'type': 'critic',
    'verified': 'false',
}


def fetch_movie_details(list_data : list):


    print("---------fetch_movie_details-----------")
    for dict_data in list_data:
        movie_detail_list = []
        id = dict_data.get("id")
        movie_name = dict_data.get("movie_name")
        movie_url = dict_data.get("movie_url")
        print("MOVIES DATA id : ", id, movie_name, movie_url)

        response = requests.get(movie_url, cookies=cookies, headers=headers)
        
        # with open("single_movie_url.html", "w", encoding="utf-8") as f:
        #     f.write(response.text)

        tree = html.fromstring(response.text)
        script = tree.xpath("//script[@data-json='mediaScorecard']/text()")
        python_dict = json.loads(script[0]) if script else None
        
        # with open("single_movie_url_json.json", "w", encoding="utf-8") as f:
        #     json.dump(python_dict, f, indent=4)
        
        movie_id = python_dict.get("criticReviewHref").split("/movie/")[-1]
        description = python_dict.get("description")
        movie_image_url = python_dict.get("primaryImageUrl")
        movie_image_url = movie_image_url if movie_image_url else ""
 
        reviews = python_dict.get("overlay").get("criticsAll").get("scoreLinkText")
        scorePercent = python_dict.get("criticsScore").get("scorePercent")

        ## cast and crew
        cast_and_crew_url = movie_url + "/cast-and-crew"
        response = requests.get(
            cast_and_crew_url,
            cookies=cookies,
            headers=headers,
        )

        # with open("single_movie_url_cast_crew.html", "w", encoding="utf-8") as f:
        #     f.write(response.text)

        tree = html.fromstring(response.text)
        cast_data = tree.xpath("//div[@data-castandcrewmanager='mediaContainer']//cast-and-crew-card[@data-castandcrewmanager='card']")

        cast_and_crew_data_list = []

        for card in cast_data:
            cast_name = card.xpath(".//rt-text[@slot='title']/text()")
            cast_name = cast_name[0] if cast_name else ""

            characters = card.xpath(".//rt-text[@slot='characters']/text()")
            characters = characters[0] if characters else ""

            credits = card.xpath(".//rt-text[@slot='credits']/text()")
            credits = credits[0] if credits else ""


            end_url = card.xpath("./@media-url")
            end_url = end_url[0] if end_url else ""

            cast_url = base_url + end_url if end_url else ""

            image_url = card.xpath(".//rt-img[@slot='poster']/@src")
            cast_image_url = image_url[0] if image_url else ""
            cast_and_crew_data_list.append({
                "cast_name" : cast_name,
                "characters" : characters,
                "credits" : credits,
                "cast_url": cast_url,
                "cast_image_url" : cast_image_url
            })

        review_headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'{movie_url}/reviews',
            'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            # 'cookie': 'akamai_generated_location={"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=82~id=118cab4333c61f05ea6abe27ceec9ef8; eXr91Jra=Az_yh6mdAQAAwf-PxK41aLz5o6LdcENLztJCK_4GFDlGXYUzqXNu3f1DoI0FAcI9KGCuco1HwH8AAEB3AAAAAA|1|0|bf1a09417dd1127b19bb88d3c28fbc3d3f4fb798; usprivacy=1---; OptanonAlertBoxClosed=2026-04-20T06:15:58.476Z; OneTrustWPCCPAGoogleOptOut=false; _ALGOLIA=anonymous-f4663f31-439d-4ae4-aaae-c028891a72d6; _cb=B2QkZ8BdmX6RBGx3nJ; check=true; algoliaUT=6a5dfa36-01f2-421a-975a-4763025bed99; __host_color_scheme=JteVcojf-1dA6QJhXuLkYossARKNVIPi4HiMhdP6Ld9NxmgKa8TM; __host_theme_options=1776666313156; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; s_cc=true; _cb_svref=external; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C15553540245624872380013280458890593436%7CMCAAMLH-1777289958%7C12%7CMCAAMB-1777289958%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776692358s%7CNONE%7CvVersion%7C4.6.0%7CMCIDTS%7C20564; s_sq=%5B%5BB%5D%5D; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+17%3A16%3A39+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=a0702456-efc5-46e1-ac26-eecf2dce2da0&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&crTime=1776665759917&geolocation=SG%3B&AwaitingReconsent=false; sailthru_pageviews=19; mbox=PC#d80507713c534d2ea8f4d09437c8b852.41_0#1839910558|session#ee78503a6b154df5b3f4fc2ee650b634#1776687460; _chartbeat2=.1776665760185.1776685600276.1.CQJ11gCcP6qXCux0BRBUmVv_DRaZik.4; _awl=2.1776685601.5-2063d19ecc891d1de23bfe2ef967bcf3-6763652d617369612d6561737431-0; __gads=ID=71e4721fefb9c8b3:T=1776665761:RT=1776685602:S=ALNI_MZWiouZQt_99XIH-B4gt0yN9fTaxA; __gpi=UID=0000126e16a0641c:T=1776665761:RT=1776685602:S=ALNI_MbQiWyRqlyBbRkqtA5nBDs8jbguOg; __eoi=ID=05032d3e4192e565:T=1776665761:RT=1776685602:S=AA-AfjaFa8qfKuX7L06bjXXUjHFN; cto_bundle=UDBiB19NaGx4bWRRVXNrQnZ2aHVoRlZoeDJ0bURvS2dsa21tS3YyaSUyQm9Eb0FLcnowU3JieFZoaUhUdXVlNUtVNnF2Mm51RnVBems0Vm1LJTJGUm9POE15Rnl1N2hPamo0dXdQdERaaWtUQmFEemlSaTZqWWhWVUtPalpLRVhyZFlPb0V4cm43NSUyRnI5MXUlMkJsTCUyRkRnT3Z0V3RkJTJGdXNDZmdIYmpQZkhrdE0lMkZvU2REYk8lMkZBJTNE; _chartbeat4=t=BLiyF_DjOOx4BhK67VDQb02BwRowo&E=6&x=333&c=0.41&y=5281&w=346',
        }


        response = requests.get(
            f'https://www.rottentomatoes.com/napi/rtcf/v1/movies/{movie_id}/reviews',
            params=review_params,
            cookies=review_cookies,
            headers=review_headers,
        )

        # with open("single_movie_url_review.html", "w", encoding="utf-8") as f:
        #     f.write(response.text)

        tree = html.fromstring(response.text)

        python_dict = json.loads(response.text)

        # with open("single_movie_url_review_json.json", "w", encoding="utf-8") as f:
        #     json.dump(python_dict, f, indent=4)

        review_data = python_dict.get("reviews")
        review_data_list = []
        for dict_data in review_data:
            name = dict_data.get("critic").get("displayName")

            review_type = dict_data.get("scoreSentiment")
            review_type_url = dict_data.get("publicationReviewUrl")

            reviewQuote = dict_data.get("reviewQuote").replace("&#44;", ",")

            language = dict_data.get("language")
            
            review_data_list.append({
                "name" : name,
                "review_type" : review_type,
                "review_type_url" : review_type_url,
                "reviewQuote" : reviewQuote,
                "language" : language
            })
        

        ## vidoes
        response = requests.get(f'{movie_url}/videos', cookies=cookies, headers=headers)
        
        # with open("single_movie_url_videos.html", "w", encoding="utf-8") as f:
        #     f.write(response.text)

        tree = html.fromstring(response.text)
        script = tree.xpath("//script[@type='application/json']/text()")

        python_dict = json.loads(script[0]) if script else None

        # with open("single_movie_url_videos_json.json", "w", encoding="utf-8") as f:
        #     json.dump(python_dict, f, indent=4)

        video_url_list = []
        if video_url_list:
            for dict_data in python_dict:
                video_title = dict_data.get("title")
                video_url = "https://www.rottentomatoes.com" + dict_data.get("videoPageUrl")

                video_url_list.append({
                    "video_title": video_title,
                    "video_url": video_url
                })
        
        movie_detail_list.append({
            "movie_name" : movie_name,
            "description" : description,
            "image_url" : movie_image_url,
            "reviews" : reviews,
            "scorePercent" : scorePercent,
            "cast_and_crew" : json.dumps(cast_and_crew_data_list),
            "review_data_details" : json.dumps(review_data_list),
            "video_url" : json.dumps(video_url_list)
        })

        insert_movie_details_table(list_data=movie_detail_list)

        update_movie_urls_status(id, "success")
        