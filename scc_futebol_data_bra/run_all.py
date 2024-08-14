import os
from datetime import date
from os import path
from scc_futebol_data_bra import get_data_download, get_data_process, commit_data


def run_all(db_folder_path, raw_folder, date):
    file_downloaded = get_data_download(date)
    sql_folder = get_data_process(file_downloaded)
    commit_data(sql_folder, db_folder_path, raw_folder)


if __name__ == '__main__':
    db_folder_path = f'{path.dirname(__file__)}/_0_in_example_db/db'
    raw_folder = f'{path.dirname(__file__)}/_0_in_example_db/raw'
    run_all(db_folder_path, raw_folder, date=date.today())
