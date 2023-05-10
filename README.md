# CeneoScraperS11

## Selektory CSS składowych opinii w serwisie Ceneo.pl

| składowa | nazwa | selektor |
| --- | --- | --- |
| opinia | opnion | div.js\_product-review |
| identyfikator opinii | opinion\_id | ["data-entry-id"] |
| autor | author | span.user-post\_\_author-name |
| rekomendacja | recommendation | span.user-post\_\_author-recomendation \> em |
| liczba gwiazdek | score | span.user-post\_\_score-count |
| czy opinia jest potwierdzona zakupem | purchased | div.review-pz |
| data wystawienia opinii | published\_at | span.user-post\_\_published \> time:nth-child(1)["datetime"] |
| data zakupu produktu | purchased\_at | span.user-post\_\_published \> time:nth-child(2)["datetime"] |
| ile osób uznało opinię za przydatną | thumbs\_up | span[id^=votes-yes]button.vote-yes["data-total-vote"]button.vote-yes \> span |
| ile osób uznało opinię za nieprzydatną | thumbs\_down | span[id^=votes-no]button.vote-no["data-total-vote"]button.vote-no \> span |
| treść opinii | content | div.user-post\_\_text |
| listę wad | cons | div.review-feature\_\_col:has(\> div.review-feature\_\_title--negatives) \> div.review-feature\_\_item |
| listę zalet | pros | div.review-feature\_\_col:has(\> div.review-feature\_\_title--positives) \> div.review-feature\_\_item |

## Użyte biblioteki
- Requests
- BeautifulSoup4
- Json
- Os
- Pandas
- Numpy
- Matplolib


# użyte biblioteki
- Requests
- BeautifulSoup4