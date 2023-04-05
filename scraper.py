import requests
from bs4 import BeautifulSoup

def get_cos(ancestor, selector = None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select("selector")].copy()
        if not selector:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None


product_code = 99105003
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"

response = requests.get(url)
page = BeautifulSoup(response.text, "html.parser")
opinions = page.select("div.js_product-review")

all_opinions = []

for opinion in opinions:
    print(opinion["data-entry-id"])
    single_opinion = {
        "opinion_id" : opinion["data-entry-id"],
        "author" : opinion.select_one("span.user-post__author-name").text.strip(),
        "recomendation" : opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "score" : opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased" : opinion.select_one("div.review-pz").text.strip(),
        "publish_date" : opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchased_at" : opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "thumbs_up" : opinion.select_one("span[id^=votes-yes]").text.strip(),
        "thumbs_down" : opinion.select_one("span[id^=votes-no]").text.strip(),
        "content" : opinion.select_one("div.user-post__text").text.strip(),
        "cons" : [cons.text.strip() for cons in opinion.select("div.review-feature__col:has(> div.review-feature title-negatives) > div.review-feature item")],
        "pros" : [pros.text.strip() for pros in opinion.select("div.review-feature__col:has(> div.review-feature title-positives) > div.review-feature item")]

    }
    print(single_opinion)
    all_opinions.append(single_opinion)

print(all_opinions)
#print(page.prettify())