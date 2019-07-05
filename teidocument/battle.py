""" Compare teidoc to tei_reader """

from tei_reader import TeiReader
from teidoc import TEIDocument

import logging
from functools import wraps
import os.path
import time


log_file = os.path.join(os.path.dirname(__file__), "teidoc.log")
FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=log_file, filemode="w", format=FORMAT, level=logging.DEBUG)


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__module__}.{func.__name__} : {end-start}\n")
        return r
    return wrapper


tei_file_path = "/Users/niels/projects/TEIDocument/teidocument/let001.xml"


@timethis
def _tei_reader():
    reader = TeiReader()
    corpora = reader.read_file(tei_file_path)  # or read_string

    print(corpora.text)


@timethis
def _tei_document():
    td = TEIDocument()
    td.load(tei_file_path)

    print("\n".join(td.text().get("original")))


if __name__ == '__main__':
    _tei_reader()
    _tei_document()
