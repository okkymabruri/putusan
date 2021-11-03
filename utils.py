import os


def create_path(destination):
    # setup path
    current_path = os.path.dirname(__file__)
    path = f"{current_path}/{destination}"

    # create folder
    if not os.path.exists(path):
        os.mkdir(path)

    print(f"save output to {path}")
    return path
