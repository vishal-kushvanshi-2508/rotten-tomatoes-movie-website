from lxml import html, etree
import os
# from parse_using_xpath import xpath_data
# from parsel import Selector
from store_data_database import *

import json

import requests

cookies = {
    'akamai_generated_location': '{"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}',
    'akacd_RTReplatform': '2147483647~rv=50~id=add1c0e998b6674fc2521f9878aea687',
    'eXr91Jra': 'Ay2Wl6mdAQAAgijs68_OfMln_XD3KDPBf4NPavN-2-KtJ3n09jWDUfhjjdo1AcI9KEKuco1HwH8AAEB3AAAAAA|1|0|1b11661af0d39f754dd72625be727da48628091b',
    '__host_color_scheme': 'WEPGy4VT-U9PSE3p9kiQYWZk9MUcGuBgOBBEPyzfbqLvaqJ83NH0',
    '__host_theme_options': '1776666778644',
    'usprivacy': '1---',
    'algoliaUT': '1e3593e0-f345-46d4-a1ab-0f5aecff9900',
    'check': 'true',
    'AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg': '1',
    's_cc': 'true',
    '_cb': 'BP1SUcD_4VWUOYSoU',
    '_ALGOLIA': 'anonymous-dcc345bb-7db5-475a-bf10-c3ca772ff5d5',
    'OptanonAlertBoxClosed': '2026-04-20T06:33:03.590Z',
    'OneTrustWPCCPAGoogleOptOut': 'false',
    'AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg': '-408604571%7CMCMID%7C01023390058502831701914582603058684230%7CMCAAMLH-1777271631%7C12%7CMCAAMB-1777271631%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1776674031s%7CNONE%7CMCSYNCSOP%7C411-20571%7CvVersion%7C4.6.0%7CMCIDTS%7C20564',
    's_sq': '%5B%5BB%5D%5D',
    'QSI_HistorySession': '',
    's_fid': '64088BDFE48B98E7-39A16E839B3585BD',
    '__gads': 'ID=cb1cee13f8be18b0:T=1776666784:RT=1776672976:S=ALNI_MY6s5UC0FsAoUHrMtIkjf90O54n1g',
    '__gpi': 'UID=0000126e1c7b0cb9:T=1776666784:RT=1776672976:S=ALNI_MZyBakDUF0nbrXq-n474hTPIm5lWw',
    '__eoi': 'ID=a154060815224710:T=1776666784:RT=1776672976:S=AA-AfjbCR_SnpCsoLW2X4V4ro8i1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+20+2026+13%3A49%3A39+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=c4b66cd6-876d-4aee-91c8-68864fda6c69&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&geolocation=SG%3B&AwaitingReconsent=false',
    'mbox': 'session#b1b1f5ba531242eb8cfc65f1a90aca85#1776675040|PC#b1b1f5ba531242eb8cfc65f1a90aca85.41_0#1839911583',
    '_chartbeat2': '.1776666782938.1776673179391.1.HU_UDCXndQvDQxhnUDdOBEOB_YUpc.1',
    '_cb_svref': 'external',
    'sailthru_pageviews': '41',
    '_awl': '2.1776673180.5-9bddadd0bfe1b77035436ad37472d8bc-6763652d617369612d6561737431-0',
    'cto_bundle': 'TmhUHl9TSjUyeWRmRkRrZm45WEVydTB2S09SWWFud2VRMVYlMkZmcHlBZndMJTJGNEc1bWV3OURvcTgyaFpNc0pJUE83NFROWUdCQVJsWjRmdFNpZHA1WWhkYjhlRkVvZE1lbGNRR3JlMlN2Vm1ic3RwdG9mTlNLY0tnckQlMkZzOUJtWFFMQTFmdQ',
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
    # 'cookie': 'akamai_generated_location={"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=50~id=add1c0e998b6674fc2521f9878aea687; eXr91Jra=Ay2Wl6mdAQAAgijs68_OfMln_XD3KDPBf4NPavN-2-KtJ3n09jWDUfhjjdo1AcI9KEKuco1HwH8AAEB3AAAAAA|1|0|1b11661af0d39f754dd72625be727da48628091b; __host_color_scheme=WEPGy4VT-U9PSE3p9kiQYWZk9MUcGuBgOBBEPyzfbqLvaqJ83NH0; __host_theme_options=1776666778644; usprivacy=1---; algoliaUT=1e3593e0-f345-46d4-a1ab-0f5aecff9900; check=true; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; s_cc=true; _cb=BP1SUcD_4VWUOYSoU; _ALGOLIA=anonymous-dcc345bb-7db5-475a-bf10-c3ca772ff5d5; OptanonAlertBoxClosed=2026-04-20T06:33:03.590Z; OneTrustWPCCPAGoogleOptOut=false; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C01023390058502831701914582603058684230%7CMCAAMLH-1777271631%7C12%7CMCAAMB-1777271631%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1776674031s%7CNONE%7CMCSYNCSOP%7C411-20571%7CvVersion%7C4.6.0%7CMCIDTS%7C20564; s_sq=%5B%5BB%5D%5D; QSI_HistorySession=; s_fid=64088BDFE48B98E7-39A16E839B3585BD; __gads=ID=cb1cee13f8be18b0:T=1776666784:RT=1776672976:S=ALNI_MY6s5UC0FsAoUHrMtIkjf90O54n1g; __gpi=UID=0000126e1c7b0cb9:T=1776666784:RT=1776672976:S=ALNI_MZyBakDUF0nbrXq-n474hTPIm5lWw; __eoi=ID=a154060815224710:T=1776666784:RT=1776672976:S=AA-AfjbCR_SnpCsoLW2X4V4ro8i1; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+13%3A49%3A39+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=c4b66cd6-876d-4aee-91c8-68864fda6c69&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&geolocation=SG%3B&AwaitingReconsent=false; mbox=session#b1b1f5ba531242eb8cfc65f1a90aca85#1776675040|PC#b1b1f5ba531242eb8cfc65f1a90aca85.41_0#1839911583; _chartbeat2=.1776666782938.1776673179391.1.HU_UDCXndQvDQxhnUDdOBEOB_YUpc.1; _cb_svref=external; sailthru_pageviews=41; _awl=2.1776673180.5-9bddadd0bfe1b77035436ad37472d8bc-6763652d617369612d6561737431-0; cto_bundle=TmhUHl9TSjUyeWRmRkRrZm45WEVydTB2S09SWWFud2VRMVYlMkZmcHlBZndMJTJGNEc1bWV3OURvcTgyaFpNc0pJUE83NFROWUdCQVJsWjRmdFNpZHA1WWhkYjhlRkVvZE1lbGNRR3JlMlN2Vm1ic3RwdG9mTlNLY0tnckQlMkZzOUJtWFFMQTFmdQ',
}





pagination_cookies = {
    'akamai_generated_location': '{"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}',
    'akacd_RTReplatform': '2147483647~rv=50~id=add1c0e998b6674fc2521f9878aea687',
    'eXr91Jra': 'Ay2Wl6mdAQAAgijs68_OfMln_XD3KDPBf4NPavN-2-KtJ3n09jWDUfhjjdo1AcI9KEKuco1HwH8AAEB3AAAAAA|1|0|1b11661af0d39f754dd72625be727da48628091b',
    '__host_color_scheme': 'WEPGy4VT-U9PSE3p9kiQYWZk9MUcGuBgOBBEPyzfbqLvaqJ83NH0',
    '__host_theme_options': '1776666778644',
    'usprivacy': '1---',
    'algoliaUT': '1e3593e0-f345-46d4-a1ab-0f5aecff9900',
    'check': 'true',
    'AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg': '1',
    's_cc': 'true',
    '_cb': 'BP1SUcD_4VWUOYSoU',
    '_ALGOLIA': 'anonymous-dcc345bb-7db5-475a-bf10-c3ca772ff5d5',
    'OptanonAlertBoxClosed': '2026-04-20T06:33:03.590Z',
    'OneTrustWPCCPAGoogleOptOut': 'false',
    'AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg': '-408604571%7CMCMID%7C01023390058502831701914582603058684230%7CMCAAMLH-1777271631%7C12%7CMCAAMB-1777271631%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1776674031s%7CNONE%7CMCSYNCSOP%7C411-20571%7CvVersion%7C4.6.0%7CMCIDTS%7C20564',
    's_fid': '64088BDFE48B98E7-39A16E839B3585BD',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+20+2026+14%3A00%3A12+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=c4b66cd6-876d-4aee-91c8-68864fda6c69&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&geolocation=SG%3B&AwaitingReconsent=false',
    'mbox': 'session#b1b1f5ba531242eb8cfc65f1a90aca85#1776675673|PC#b1b1f5ba531242eb8cfc65f1a90aca85.41_0#1839911583',
    'sailthru_pageviews': '45',
    '_chartbeat2': '.1776666782938.1776673816058.1.DmgE5-D-7geOc5Cm4sQ1ZIDAxJmP.1',
    '_cb_svref': 'external',
    '__gads': 'ID=cb1cee13f8be18b0:T=1776666784:RT=1776673819:S=ALNI_MY6s5UC0FsAoUHrMtIkjf90O54n1g',
    '__gpi': 'UID=0000126e1c7b0cb9:T=1776666784:RT=1776673819:S=ALNI_MZyBakDUF0nbrXq-n474hTPIm5lWw',
    '__eoi': 'ID=a154060815224710:T=1776666784:RT=1776673819:S=AA-AfjbCR_SnpCsoLW2X4V4ro8i1',
    'cto_bundle': 'Smm28l9TSjUyeWRmRkRrZm45WEVydTB2S09jdzhRZWpJM01ZUDg5cHNGeiUyRlhRUHU2SldZZ2dkWGR2cmtaek1Gd1NMN3BWQXZUV3AlMkJ3biUyRk5lUVlDMnpBU1BHT2NXWUI3ZG81N2phUGNiT1p1SGoySktreDBzRnFnbEhjdyUyQnJXUXlxazNP',
    '_awl': '2.1776673826.5-9bddadd0bfe1b77035436ad37472d8bc-6763652d617369612d6561737431-0',
    's_sq': 'wbrosrottentomatoes%3D%2526c.%2526a.%2526activitymap.%2526page%253Drt%252520%25257C%252520browse%252520%25257C%252520list%252520page%252520%25257C%252520movies%252520in%252520theaters%2526link%253DLOAD%252520MORE%2526region%253Dmain-page-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Drt%252520%25257C%252520browse%252520%25257C%252520list%252520page%252520%25257C%252520movies%252520in%252520theaters%2526pidt%253D1%2526oid%253DLOAD%252520MORE%2526oidt%253D3%2526ot%253DSUBMIT',
}

pagination_headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page=2',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': 'akamai_generated_location={"zip":"""","city":"MUMBAI","state":"MH","county":"""","areacode":"""","lat":"18.98","long":"72.83","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=50~id=add1c0e998b6674fc2521f9878aea687; eXr91Jra=Ay2Wl6mdAQAAgijs68_OfMln_XD3KDPBf4NPavN-2-KtJ3n09jWDUfhjjdo1AcI9KEKuco1HwH8AAEB3AAAAAA|1|0|1b11661af0d39f754dd72625be727da48628091b; __host_color_scheme=WEPGy4VT-U9PSE3p9kiQYWZk9MUcGuBgOBBEPyzfbqLvaqJ83NH0; __host_theme_options=1776666778644; usprivacy=1---; algoliaUT=1e3593e0-f345-46d4-a1ab-0f5aecff9900; check=true; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; s_cc=true; _cb=BP1SUcD_4VWUOYSoU; _ALGOLIA=anonymous-dcc345bb-7db5-475a-bf10-c3ca772ff5d5; OptanonAlertBoxClosed=2026-04-20T06:33:03.590Z; OneTrustWPCCPAGoogleOptOut=false; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C01023390058502831701914582603058684230%7CMCAAMLH-1777271631%7C12%7CMCAAMB-1777271631%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1776674031s%7CNONE%7CMCSYNCSOP%7C411-20571%7CvVersion%7C4.6.0%7CMCIDTS%7C20564; s_fid=64088BDFE48B98E7-39A16E839B3585BD; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+14%3A00%3A12+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=c4b66cd6-876d-4aee-91c8-68864fda6c69&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1%2C1%3A1&iType=1&intType=1&geolocation=SG%3B&AwaitingReconsent=false; mbox=session#b1b1f5ba531242eb8cfc65f1a90aca85#1776675673|PC#b1b1f5ba531242eb8cfc65f1a90aca85.41_0#1839911583; sailthru_pageviews=45; _chartbeat2=.1776666782938.1776673816058.1.DmgE5-D-7geOc5Cm4sQ1ZIDAxJmP.1; _cb_svref=external; __gads=ID=cb1cee13f8be18b0:T=1776666784:RT=1776673819:S=ALNI_MY6s5UC0FsAoUHrMtIkjf90O54n1g; __gpi=UID=0000126e1c7b0cb9:T=1776666784:RT=1776673819:S=ALNI_MZyBakDUF0nbrXq-n474hTPIm5lWw; __eoi=ID=a154060815224710:T=1776666784:RT=1776673819:S=AA-AfjbCR_SnpCsoLW2X4V4ro8i1; cto_bundle=Smm28l9TSjUyeWRmRkRrZm45WEVydTB2S09jdzhRZWpJM01ZUDg5cHNGeiUyRlhRUHU2SldZZ2dkWGR2cmtaek1Gd1NMN3BWQXZUV3AlMkJ3biUyRk5lUVlDMnpBU1BHT2NXWUI3ZG81N2phUGNiT1p1SGoySktreDBzRnFnbEhjdyUyQnJXUXlxazNP; _awl=2.1776673826.5-9bddadd0bfe1b77035436ad37472d8bc-6763652d617369612d6561737431-0; s_sq=wbrosrottentomatoes%3D%2526c.%2526a.%2526activitymap.%2526page%253Drt%252520%25257C%252520browse%252520%25257C%252520list%252520page%252520%25257C%252520movies%252520in%252520theaters%2526link%253DLOAD%252520MORE%2526region%253Dmain-page-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Drt%252520%25257C%252520browse%252520%25257C%252520list%252520page%252520%25257C%252520movies%252520in%252520theaters%2526pidt%253D1%2526oid%253DLOAD%252520MORE%2526oidt%253D3%2526ot%253DSUBMIT',
}



def extract_movies_url():

    print("---------parse-----------")
    # print("response : ", response.text)

    response = requests.get(
        'https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest',
        cookies=cookies,
        headers=headers,
    )

    # print("response : ", response)
    # with open("movies_in_theaters.html", "w", encoding="utf-8") as f:
    #     f.write(response.text)

    tree = html.fromstring(response.text)
    next_page = tree.xpath("//script[@id='pageInfo']/text()")
    next_page = next_page[0] if next_page else None 
    next_page_data = json.loads(next_page)
    next_page_id = next_page_data.get("endCursor")

    
    # print("next_page_id : ", next_page_data)
    

    script = tree.xpath("//script[@type='application/ld+json']/text()")
    script_data = script[0] if script else None 
    # print("script_data : ", script_data)
    # print("script_data : ", type(script_data))
    
    python_dict = json.loads(script_data)

    # print("python_dict : ", python_dict)
    # print("python_dict : ", type(python_dict))

    # with open("movies_json_data.json", "w", encoding="utf-8") as f:
    #     json.dump(python_dict, f, indent=4)

    # itemListElement.itemListElement
    itemListElement = python_dict.get("itemListElement", []).get("itemListElement", [])
    # print(itemListElement)
    # print(len(itemListElement))
    
    movies_data_list = []
    for dict_data in itemListElement:
        movie_name = dict_data.get("name")
        movie_url = dict_data.get("url")
        movies_data_list.append({
            "movie_name": movie_name,
            "movie_url": movie_url,
            "status" : "pending"
        })
    
    # print(movies_data_list)
    # print(len(movies_data_list))

    if movies_data_list:
        # print("database enter : ")
        insert_movie_urls_table(list_data=movies_data_list)

        movies_data_list.clear()

    # print("next : ", movies_data_list)
    # print(len(movies_data_list))

    # print("next_page_id : ", next_page_id)


    while True:


        params = {
            'after': next_page_id,
        }

        response = requests.get(
            'https://www.rottentomatoes.com/cnapi/browse/movies_in_theaters/sort:newest',
            params=params,
            cookies=pagination_cookies,
            headers=pagination_headers,
        )

        python_dict = json.loads(response.text)
        
        with open("movies_json_data2.json", "w", encoding="utf-8") as f:
            json.dump(python_dict, f, indent=4)

        # itemListElement.itemListElement
        itemListElement = python_dict.get("grid", []).get("list", [])
        # print(itemListElement)
        # print(len(itemListElement))
        
        if not itemListElement: 
            # print("not more data found " )
            break

        next_page_id = python_dict.get("pageInfo", {}).get("endCursor")


        
        
        for dict_data in itemListElement:
            movie_name = dict_data.get("title")
            movie_url = r"https://www.rottentomatoes.com" + dict_data.get("mediaUrl")
            # print(movie_name,movie_url)
            movies_data_list.append({
                        "movie_name": movie_name,
                        "movie_url": movie_url,
                        "status" : "pending"
                    })
                
        # print(movies_data_list)
        # print(len(movies_data_list))

        if movies_data_list:
            insert_movie_urls_table(list_data=movies_data_list)
            movies_data_list.clear()

    




    print("---------parse end-----------")






# ## get html content using url

# # def read_html_content(url):
# #     headers = {
# #         "User-Agent": "Mozilla/5.0"
# #     }
# #     response = requests.get(url, headers=headers)
# #     tree = html.fromstring(response.text)

# #     # convert to formatted HTML
# #     formatted_html = etree.tostring(tree, pretty_print=True, encoding="unicode")
# #     with open("wendys_html_content.html", "w", encoding="utf-8") as f:
# #         f.write(formatted_html)
# #     return formatted_html


# ## get html content using direct file

# def read_html_content(file_name):
#     current_working_dir = os.getcwd()
#     file_path = f"{current_working_dir}/{file_name}"
#     with open(file_path, "r", encoding='utf-8') as f :
#         html_content = f.read()
#     return html_content

# def extract_data_from_html(html_content):
#     product_list = []
#     tree = html.fromstring(html_content)
#     milk_data = tree.xpath(xpath_data.get("amul_gold_data"))
#     milk_data_dict = json.loads(milk_data)
#     data = Selector(json.dumps(milk_data_dict))
#     amul_gold_data={}
#     amul_gold_data["Product_Name"]=data.jmespath("[0].name").get()

#     amul_gold_data["Brand_Name"]=data.jmespath("[0].brand.name").get()

#     amul_gold_data["Product_Id"]=data.jmespath("[0].sku").get()

#     amul_gold_data["Description"]=data.jmespath("[0].description").get()

#     img= data.jmespath("[0].image").getall()
#     amul_gold_data["Images"]=json.dumps(img)

#     amul_gold_data["Category"]=data.jmespath("[0].category").get()   

#     amul_gold_data["Rating"]=data.jmespath("[0].aggregateRating.ratingValue").get()

#     amul_gold_data["Review_Count"]=data.jmespath("[0].aggregateRating.reviewCount").get()

#     amul_gold_data["Rating_Count"]=data.jmespath("[0].aggregateRating.ratingCount").get()

#     amul_gold_data["Price"]=data.jmespath("[0].offers.price").get()

#     amul_gold_data["Currency"]=data.jmespath("[0].offers.priceCurrency").get()

#     amul_gold_data["Avl_Url"]=data.jmespath("[0].offers.availability").get()

#     amul_gold_data["Item_Condition"]=data.jmespath("[0].offers.itemCondition").get()
#     return_policies_data={
#         "Url":data.jmespath("[0].offers.hasMerchantReturnPolicy.url").get(),
#         "Descrition":data.jmespath("[0].offers.hasMerchantReturnPolicy.description").get(),
#         "Applicable_Country":data.jmespath("[0].offers.hasMerchantReturnPolicy.applicableCountry").get(),
#         "Return_Category":data.jmespath("[0].offers.hasMerchantReturnPolicy.returnPolicyCategory").get()
#     }

#     amul_gold_data["Return_Policy"]=json.dumps(return_policies_data)
#     product_list.append(amul_gold_data)
#     return product_list
#     # 