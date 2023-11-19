import pickle


def store(data):
    with open("data.pkl", "wb") as file:
        pickle.dump(data, file)


def restore():
    with open("data.pkl", "rb") as file:
        loaded_data = pickle.load(file)
        return loaded_data
