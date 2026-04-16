import pandas as pd


def load_sample(file_path, nrows=100000):
    # Load a limited number of rows from compressed dataset for quick inspection
    return pd.read_csv(
        file_path,
        compression="gzip",
        nrows=nrows
    )