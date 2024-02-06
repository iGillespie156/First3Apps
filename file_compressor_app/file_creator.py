import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as myzip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            myzip.write(filepath, arcname=filepath.name)



if __name__ == "__main__":
    make_archive(filepaths=["file_creator.py", 'gui.py'], dest_dir = "")