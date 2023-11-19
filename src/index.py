import yake

from db import insert, search

def extract(msg: str):
    numOfKeywords = 3
    kw_extractor = yake.KeywordExtractor(top=numOfKeywords)
    keywords = kw_extractor.extract_keywords(msg)
    return keywords


def print_dict(table):
    # Printing the entire table in a useful view
    print("\nComplete Table View:")
    for keyphrase, treemap in table.items():
        print(f"Keyphrase: '{keyphrase}'")

        # Sorting the treemap based on scores (values) in descending order
        sorted_treemap = sorted(treemap.items(), key=lambda item: item[1])

        for message, score in sorted_treemap:
            print(f"  Score: {score}, Message: '{message}'")

