import pandas as pd
from src.etl.transform import transform_chunk


def run_etl(input_path: str, output_path: str, chunksize: int = 100000):
    # Process large dataset in chunks
    chunk_iter = pd.read_csv(
        input_path,
        compression="gzip",
        chunksize=chunksize
    )

    processed_chunks = []

    for chunk in chunk_iter:
        # Transform each chunk
        transformed = transform_chunk(chunk)
        processed_chunks.append(transformed)

    # Combine all chunks
    final_df = pd.concat(processed_chunks, ignore_index=True)

    # Save to parquet
    final_df.to_parquet(output_path, index=False)


if __name__ == "__main__":
    input_path = "data/raw/2019-Dec.csv.gz"
    output_path = "data/processed/2019-Dec.parquet"

    run_etl(input_path, output_path)