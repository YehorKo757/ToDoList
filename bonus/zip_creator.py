import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=["quiz_app.py", "questions.json"], dest_dir="compressed_quiz")
