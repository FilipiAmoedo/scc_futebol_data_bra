from os import path
from cli_commit import apply_db, copy_files
from scc_futebol_data_bra.env import DB_NAME


def commit_data(data_temp_folder, db_folder_path, raw_folder):
    copy_files(data_temp_folder + '/raw/', raw_folder)
    db_path = path.join(db_folder_path, DB_NAME)
    apply_db(data_temp_folder + '/sql/', db_path)
if __name__ == '__main__':
    sql_folder = f'{path.dirname(__file__)}/_example_file'
    result_folder = f'{path.dirname(path.dirname(__file__))}/_0_in_example_db'
    commit_data(sql_folder, result_folder + '/db', result_folder + '/raw')