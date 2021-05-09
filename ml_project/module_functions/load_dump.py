import pickle


def load_model(file_name: str):
    with open(file_name, 'rb') as handle:
        model = pickle.load(handle)
    return model


def dump_model(file_name: str, obj: object):
    with open(file_name, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)