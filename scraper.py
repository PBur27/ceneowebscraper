import requests
import json
from bs4 import BeautifulSoup


def get_element(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None


selectors = {
    "opinion_id": [None, "data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recomendation": ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "purchased": ["div.review-pz"],
    "publish_date": ["span.user-post__published > time:nth-child(1)","datetime"],
    "purchased_at": ["span.user-post__published > time:nth-child(2)","datetime"],
    "thumbs_up": ["span[id^=votes-yes]"],
    "thumbs_down": ["span[id^=votes-no]"],
    "content": ["div.user-post__text"],
    "pros": ["div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item",None, True],
    "cons": ["div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item",None, True]
}

product_code = 99105003
all_opinions = []
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

while url:
    print(url)
    response = requests.get(url)
    if response.status_code == 301:
        break
    page = BeautifulSoup(response.text, "html.parser")
    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = get_element(opinion, *value)
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl/"+get_element(page, "a.pagination__next", "href")
    except TypeError:
        url = None

print(len(all_opinions))
with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
# print(page.prettify())
