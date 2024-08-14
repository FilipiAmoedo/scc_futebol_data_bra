import pandas as pd



def read_excel(file_path) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['ID'] = range(1, len(df) + 1)
    df.drop(columns=['Time'], inplace=True)
    return df

if __name__ == '__main__':
    from os import path
    filepath = path.join(path.dirname(__file__), '_example_file', 'BRA_2023-10-24.xlsx')
    print(read_excel(filepath))
