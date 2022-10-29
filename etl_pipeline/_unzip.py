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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, FOLDER_PATH)

    os.system("rm *.txt")
    os.system("rm *.tar.gz")


if __name__ == '__main__':
    run(os.environ.get("HOME"))
