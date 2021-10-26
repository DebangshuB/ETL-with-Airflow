import os
import tarfile

"""
    This function downloads tha data from the url and unzips it.
"""


def run(HOME):

    os.chdir(os.path.join(HOME, "data"))
    os.rename(os.listdir()[0], "_data.tar.gz")

    FOLDER_PATH = os.path.join(HOME, "data")

    with tarfile.open(os.path.join(FOLDER_PATH, "_data.tar.gz"), 'r:gz') as tar:
        tar.extractall(FOLDER_PATH)

    os.system("rm *.txt")
    os.system("rm *.tar.gz")


if __name__ == '__main__':
    run(os.environ.get("HOME"))
