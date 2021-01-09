import json
from pprint import pprint

with open("newsafr.json", encoding='utf-8') as f:
    data = json.load(f)
    all_news = data['rss']["channel"]["items"]
    all_words = []
    for news in all_news:
        words = news['description'].split()
        for word in words:
            all_words.append(word)
    all_words.sort()


def find_specified_length(some_text, word_length):
    words_sort = []
    for elem in some_text:
        if len(elem) > word_length:
            words_sort.append(elem)
    return words_sort


def find_words_count(some_list, limit):
    content = {}
    for elem in some_list:
        if elem in content.keys():
            content[str(elem)] += 1
        else:
            content[str(elem)] = 1
    sorted_list = sorted(content, key=content.get, reverse=True)[:limit]
    print('Для файла "newsafr.json"')
    for x in sorted_list:
        if x in content.keys():
            print(f'{x.upper()}  встречается {content[x]} раз')
    return content


sort_list = find_specified_length(all_words, 6)
find_words_count(sort_list, 10)

