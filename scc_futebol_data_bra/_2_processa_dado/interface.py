import os
import shutil
from os import path
from scc_futebol_data_bra._2_processa_dado._read_excel import read_excel
from scc_futebol_data_bra.api_folder_helper import get_result_folder
from scc_futebol_data_bra._2_processa_dado._create_db_sql import create_db_file
from scc_futebol_data_bra.env import TABLE_NAME


def _create_insert_sql(df):
    insert_sql = f"""INSERT OR IGNORE INTO {TABLE_NAME}
                    (Country, League, Season, Date, Home, Away, HG, AG,
                    Res, PH, PD, PA, MaxH, MaxD, MaxA, AvgH, AvgD, AvgA, BFEH, BFED, BFEA, ID) VALUES
                """

    values = []
    for index, row in df.iterrows():
        value_str = ', '.join([f"'{str(row[col])}'" for col in df.columns])
        values.append(f"({value_str})")

    return insert_sql + ",\n".join(values) + ";"


def _save_sql_insert(result_folder, data_str, df):
    sql_str = _create_insert_sql(df)
    with open(f'{result_folder}/sql/sql_insert_{data_str}.sql', 'w') as f:
        f.write(sql_str)


def _save_raw_files(result_folder, arquivos_baixados_folder, file_name):
    os.makedirs(f'{result_folder}/raw/', exist_ok=True)
    shutil.copyfile(f'{arquivos_baixados_folder}/{file_name}', f'{result_folder}/raw/{file_name}')


def get_data_process(arquivos_baixados_folder, debug_local=False):
    result_folder = get_result_folder(debug_local)
    file_name_list = [x for x in os.listdir(arquivos_baixados_folder) if 'xlsx' in x]
    assert len(file_name_list) == 1
    file_name = file_name_list[0]
    data_str = file_name.split('_')[1].replace('.xlsx', '')
    os.makedirs(f'{result_folder}/sql/', exist_ok=True)
    create_db_file(result_folder + '/sql')
    _save_raw_files(result_folder, arquivos_baixados_folder, file_name)
    df_values = read_excel(f'{arquivos_baixados_folder}/{file_name}')
    _save_sql_insert(result_folder, data_str, df_values)
    return result_folder


if __name__ == '__main__':
    filepath = path.join(path.dirname(__file__), '_example_file')
    print(get_data_process(filepath, True))
