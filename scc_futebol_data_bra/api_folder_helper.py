from os import path
import tempfile


def get_result_folder(debug_local):
    if debug_local:
        result_folder = path.dirname(__file__)
    else:
        result_folder = tempfile.mkdtemp()
    return result_folder
