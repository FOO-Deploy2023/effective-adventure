import yake


def extract(msg: str, table):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(msg)

    print(msg)
    for kw in keywords:
        keyphrase, score = kw

        treemap_val = table[keyphrase]
        treemap_val[score] = msg

        print(kw)


def print_dict(table):
    # Printing the entire table in a useful view
    print("\nComplete Table View:")
    for keyphrase, treemap in table.items():
        print(f"Keyphrase: '{keyphrase}'")
        for score, message in treemap.items():
            print(f"  Score: {score}, Message: '{message}'")
