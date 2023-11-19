import yake

from collections import defaultdict

from db import store

def extract(msg: str):
    kw_extractor = yake.KeywordExtractor()
    return kw_extractor.extract_keywords(msg)


def build(msg: str, table):
    keywords = extract(msg)

    for kw in keywords:
        print(kw)
        keyphrase = kw[0]

        if keyphrase not in table:
            table[keyphrase] = set()

        table[keyphrase].add(msg)

    print()
    return table


# def answer(msg: str, table):
#     answers = defaultdict(dict)
#     keywords = extract(msg)


def print_dict(table):
    for keyphrase, messages in table.items():
        print(f"Keyword: '{keyphrase}'")
        for msg in messages:
            print(f"  - {msg}")
        print()  # Adds an empty line for better readability
