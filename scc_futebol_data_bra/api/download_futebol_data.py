import requests
from os import path
import tempfile


URL = 'https://www.football-data.co.uk/new/BRA.xlsx'


def download_football_excel():
    temp_dir = tempfile.mkdtemp()
    r = requests.get(url=URL)
    if r.status_code == 200:
        local_filename = path.join(temp_dir, 'BRA.xlsx')
        with open(local_filename, 'wb') as file:
            file.write(r.content)
    return local_filename


if __name__ == '__main__':
    date = '23-10-2023'
    print(download_football_excel())
