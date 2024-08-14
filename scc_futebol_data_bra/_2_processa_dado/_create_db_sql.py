from os import path
from scc_futebol_data_bra.env import TABLE_NAME



def _create_db_sql():
    return f"""CREATE TABLE {TABLE_NAME}(
                Country TEXT,
                League TEXT,
                Season TEXT,
                Date TEXT,
                Home TEXT,
                Away TEXT,
                HG TEXT,
                AG TEXT,
                Res TEXT,
                PH TEXT,
                PD TEXT,
                PA TEXT,
                MaxH TEXT,
                MaxD TEXT,
                MaxA TEXT,
                AvgH TEXT,
                AvgD TEXT,
                AvgA TEXT,
                BFEH TEXT,
                BFED TEXT,
                BFEA TEXT,
                ID TEXT,
                PRIMARY KEY (ID)
    
    );
    """

def create_db_file(folder_to_save):
    with open(path.join(folder_to_save, f'sql_create_db.sql'), 'w') as file:
        file.write(_create_db_sql())
