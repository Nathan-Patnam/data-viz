
import sys
import requests
import json

def get_results(query ="", tags=[]):

    query_string = get_query_string(query, tags)
    for i in tags:
        query += i
    search_results = requests.get(query_string)

    for item in decode_response(search_results.content):
        if 'pagemap' in item:
            image_path = item['pagemap']
            if 'metatags' in image_path:
                image_url = image_path['metatags']
                print(image_url[0]['og:image'])
     
    return results

def get_query_string(query = "", tags=[]):
    api_key = "AIzaSyCYq06CBnnF27kRI_RNnhz3S0KoQPH1cNM"
    search_engine_key = "&cx=005712099980169065800:ug7myqa_ep0"
    query_string = "https://www.googleapis.com/customsearch/v1?key="
    query_string+=api_key
    query_string+=search_engine_key
    query_string+= "&q=" + query
    return query_string

def decode_response(json_string):
    response = json.loads(json_string)
    meta = {key: value for key, value in response.items() if key != 'items'}
    num_results = int(meta['searchInformation']['totalResults'])
    print("number of results is")
    if num_results == 0:
        return []
    for item in response['items']:
        item['meta'] = meta
    return response['items']

# get_results("'chart' unemployment during 2005 in USA", ["United States of America", "Trump", ""])
images = get_results("USA election 2.4 million new jobs", ["Trump", "November 2016", "jobs"])

if len(images) > 2:
    for i in images[:2]:
        print(i)
else:
    print(images[0])
    print(images[1])
