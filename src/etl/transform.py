import pandas as pd


def transform_chunk(df: pd.DataFrame) -> pd.DataFrame:
    # Select required columns
    columns = [
        "event_time",
        "event_type",
        "product_id",
        "category_id",
        "category_code",
        "brand",
        "price",
        "user_id",
        "user_session"
    ]
    
    df = df[columns]

    # Convert event_time to datetime
    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

    # Ensure price is numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Remove exact duplicate rows
    df = df.drop_duplicates()

    return df