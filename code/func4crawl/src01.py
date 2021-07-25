templat_query_cond = {
    "criteria": {
        "from": 0,
        "size": 1,
        "query": "keyword",
        "tags": None,
        "categories": None,
        "durations": [
            {"min": 120, "max": 300},
            {"min": 60, "max": 120},
            {"min": 30, "max": 60},
            {"min": 10, "max": 30},
            {"min": 0, "max": 9}
        ],
        "continents": None,
        "sortBy": None,
        "source": None,
        "recordist": None,
        "habitat": None
    }
}

def query_cond(keyword):
    templat_query_cond['criteria']['query'] = keyword
    return(templat_query_cond)

def cond_filter(keyword, response_json):
    res = []
    res.append([keyword in ' '.join(x['tags']).lower() for x in response_json['results']])
    res.append([keyword in x['description'].lower() for x in response_json['results']])
    return(res)


'''
下載 wav 檔，並且存到對應的資料夾。
'''
import requests
def download_wav(url, wav_id, filepath):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Download Failed For File {wav_id}")

