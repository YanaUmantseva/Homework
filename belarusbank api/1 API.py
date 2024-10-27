from collections import Counter
import requests

a = requests.get("https://belarusbank.by/api/news_info")
print(a)
news= a.json()

first_20_news = news[:20]
for new in first_20_news:
    print(new)

filtered_news = []
for new_even in news:
    even_date = new_even['start_date'][-1]
    if int(even_date) % 2 == 0:
        filtered_news.append(new_even)

first_20_filtered_news = filtered_news[:20]

longest_text = max(news, key=lambda x: len(x['html_ru'])) ['html_ru']
print(longest_text)

longest_name = max(news, key=lambda x: len(x['name_ru'].split())) ['name_ru']
print(longest_name)

rus_letters = Counter(''.join([new['html_ru'] for new in news]))
print(rus_letters.most_common())




