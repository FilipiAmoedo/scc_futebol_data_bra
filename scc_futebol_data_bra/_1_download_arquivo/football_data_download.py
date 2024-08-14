import pandas as pd
from datetime import date
import os
from scc_futebol_data_bra.api.download_futebol_data import download_football_excel
from scc_futebol_data_bra.api_folder_helper import get_result_folder


def _dump_excel(excel, date, folder_path):
    df = pd.read_excel(excel)
    os.makedirs(folder_path, exist_ok=True)
    filepath = os.path.join(folder_path, f'BRA_{date}.xlsx')
    df.to_excel(filepath, index=False)


def get_data_and_save(date, folder_path):
    excel_download = download_football_excel()
    _dump_excel(excel_download, date, folder_path)


def get_data_download(date, debug_local=False):
    result_folder = get_result_folder(debug_local)
    get_data_and_save(date, result_folder)
    return result_folder

if __name__ == '__main__':
    date = date.today()
    print(get_data_download(date))

