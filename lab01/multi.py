import pandas as pd
import os
from multiprocessing import Pool
from datetime import datetime


def read_file(file):
    return pd.read_csv(file)


def load_files(directory, processes):
    files = [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".csv")
    ]

    print("Liczba plików:", len(files))
    print("Liczba procesów:", processes)

    start = datetime.now()

    with Pool(processes=processes) as pool:
        dataframes = pool.map(read_file, files)

    df = pd.concat(dataframes, ignore_index=True)

    time = datetime.now() - start

    print("Czas:", time)

    return df, time


if __name__ == "__main__":
    try:
        df_multi, time_multi = load_files(
            "csv_parts",
            14
        )

        print("Czas końcowy:", time_multi)

    except Exception as e:
        print("Nie udało się wykonać testu:")
        print(type(e).__name__, e)