def extract_post(posts):
    tmp_post = []
    for x in posts:
        post_id = x.find('audio').get('id')
        download_link = x.find('audio').text
        title = {
            'text': x.find('div',{'class':'sound-effect-title'}).text,
            'link': x.find('div',{'class':'sound-effect-title'}).find('a').get('href')
        }
        tags = [i_tags.text.lower() for i_tags in x.find('div',{'class':'tag-hyperlink-container'}).find_all('a')]
        categories = [i.text.lower() for i in x.find('div',{'class':'soundeffect-categories'}).find_all('a')]
        tmp_post = tmp_post + [{'post_id': post_id, 
                                'download_link': download_link,
                                'title': title,
                                'tags': tags,
                                'categories': categories}]
    return(tmp_post)

import requests
def download_mp3(url, mp3_link, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Download Failed For File {mp3_link}")