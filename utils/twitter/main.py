import requests
import dotenv
import logging
import re
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ADD_THOUGHTS = True

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

IDS = [
    (1,1543250339385823232), # 1 none
    (2,1543252557954514944), # 2 none
    (3,1544366260342890497), # 3 web
    (4,1544758709561303041), # 4 web
    (5,1545117522613207043), # 5 img
    (6,1545446006136897536), # 6 no attachment
    (7,1547713647815733250), # 7 web
    (8,1547993617137954822), # 8 web, img
]

def get_tweet(id):
    url=f"https://api.twitter.com/2/tweets/{id}?tweet.fields=attachments,created_at,entities,source,text&expansions=attachments.media_keys&media.fields=alt_text,media_key,type,url,variants&user.fields=created_at,id,name,url,username"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    tweet = requests.get(url, headers=headers).json()
    logger.info("Got data for id:%s data:%s", id, tweet)
    return tweet

def get_text(tweet):
    return tweet.get('data').get('text')

def get_created_date(tweet):
    return tweet.get('data').get('created_at')

def download_image_attachment(daynum, tweet):
    includes = tweet.get('includes')
    if includes is None:
        return None
    media = includes.get('media')
    if ((media is None) or len(media) == 0):
        return None
    result = None
    for item in media:
        if item.get('type') == "photo":
            url = item.get('url')
            alt_text = item.get('alt_text')
            filepath = f"assets/day-{daynum}.jpg"
            result = {
                'url': url,
                'alt_text': alt_text,
                'filepath': filepath,
            }
            logger.info("Image Attachment found", result)
            response = requests.get(url)
            with open(f"../../{filepath}", "wb") as attachment:
                attachment.write(response.content)
            logger.info("Attachment saved to %s", filepath)
            break # stop at first attachment
    return result

def get_web_attachment_url(tweet):
    data=tweet.get('data')
    entities = data.get('entities')
    if entities is None:
        return None
    urls = entities.get('urls')
    if (urls is None) or (len(urls) == 0):
        return None
    result = None
    for item in urls:
        if item.get('media_key'):
            # ignore image attachment
            continue
        result = {
            'title': item.get('title'),
            'url': item.get('expanded_url'),
        }
        logger.info("Web Attachment found %s", result)
        break # stop at first
    return result

def get_last_visited_day():
    with open("./LAST_DAY", 'r') as lastday:
        data = lastday.readline()
        return int(data)
    return None

def update_last_line(num):
    with open("./LAST_DAY", 'w') as lastday:
        lastday.write(str(num))

def update_log(tweet_id, daynum, created_date,txt,web_attachment,image_attachment):
    formatted_date = created_date.split("T")[0]
    formatted_text = txt
    formatted_text = re.sub('https://t.co/\w+\s*', '', formatted_text) # remove twitter attachment links
    formatted_text = re.sub(r'([#@]\w+)', r'`\1`', formatted_text) # wrap hashtags and mentions in blocks
    formatted_text = formatted_text.strip()
    daylog = f"""
## Day {daynum}: {formatted_date}

[Tweet](https://twitter.com/BudavariMatyas/status/{tweet_id})

**Today's Progress**: {formatted_text}

"""
    if ADD_THOUGHTS:
        daylog += """**Thoughts**:
"""
    if not web_attachment is None:
     daylog += f"""
**Link(s) to work**: [{web_attachment.get('title')}]({web_attachment.get('url')})
"""
    if not image_attachment is None:
     daylog += f"""
![{image_attachment.get('alt_text')}]({image_attachment.get('filepath')})
"""

    with open("../../log.md", 'a') as lastday:
        lastday.write(daylog)

def main():
    last_day = get_last_visited_day()
    logger.info("Last visited day is: %d", last_day)
    for [daynum, id] in IDS:
        if daynum <= last_day:
            continue
        logger.info("Getting info for day: %d (id: %s)", daynum, id)
        tweet = get_tweet(id)

        txt = get_text(tweet)
        created_date = get_created_date(tweet)
        web_attachment = get_web_attachment_url(tweet)
        image_attachment = download_image_attachment(daynum, tweet)

        update_log(id, daynum, created_date,txt,web_attachment,image_attachment)
        update_last_line(daynum)

    logger.info("DONE")

if __name__ == '__main__':
    main()