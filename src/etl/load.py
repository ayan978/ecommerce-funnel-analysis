import pandas as pd


def save_to_parquet(df: pd.DataFrame, output_path: str):
    # Save dataframe to parquet file
    df.to_parquet(output_path, index=False)