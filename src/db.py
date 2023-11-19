from tinydb import TinyDB, Query


db = TinyDB("db.json")
Tree = Query()


def insert(key, tree_map):
    db.insert({"key": key, "value": tree_map})


def search(key):
    result = db.search(Tree.key == key)
    if result:
        retrieved_tree_map = result[0]["value"]

    return result
