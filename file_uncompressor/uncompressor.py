import zipfile
import pathlib

def uncompress(archive,filepath):

    with zipfile.ZipFile(archive, 'r') as zip_ref:
        zip_ref.extractall(filepath)