import yake

def extract(msg: str, table):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(msg)

    print(msg)
    for kw in keywords:
        keyphrase, score = kw

        inner_table = table[keyphrase]
        inner_table[msg] = score

        print(kw)


def print_dict(table):
    # Printing the entire table in a useful view
    print("\nComplete Table View:")
    for keyphrase, treemap in table.items():
        print(f"Keyphrase: '{keyphrase}'")

        # Sorting the treemap based on scores (values) in descending order
        sorted_treemap = sorted(treemap.items(), key=lambda item: item[1])

        for message, score in sorted_treemap:
            print(f"  Score: {score}, Message: '{message}'")

