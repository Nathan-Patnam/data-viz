
import sys
import requests
import json
def get_data(query =""):
   api_key = "AIzaSyCYq06CBnnF27kRI_RNnhz3S0KoQPH1cNM"
   search_engine_key = "&cx=005712099980169065800:ug7myqa_ep0"


   query_string = "https://www.googleapis.com/customsearch/v1?key="
   query_string+=api_key
   query_string+=search_engine_key
   query_string+= "&q=" + query

   search_results = requests.get(query_string)
   for item in _decode_response(search_results.content):
       print (item)





def _decode_response(json_string):
    response = json.loads(json_string)
    meta = {key: value for key, value in response.items() if key != 'items'}
    num_results = int(meta['searchInformation']['totalResults'])
    print("number of results is")
    if num_results == 0:
        return []
    for item in response['items']:
        item['meta'] = meta
    return response['items']
get_data("pizza")
