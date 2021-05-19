import os
from datetime import datetime

import pandas as pd
from pandas.core.frame import DataFrame


def main():
    """Main entry point for the application"""

    # Iterate through directory
    for subdir, dirs, files in os.walk("TestData"):

        # If we don't have any files, keep going.
        if files == []:
            continue

        # If we do, iterate the files
        for file in files:
            # Open the file
            filepath = subdir + os.sep + file
            df = read_csv(filepath)

            # Print the path
            print("{} - {} - {}".format(datetime.now(), df.size, filepath))


def read_csv(filepath: str) -> DataFrame:
    """Reads a given csv filepath to Pandas Dataframe

    Args:
        filepath (str): CSV Filepath

    Returns:
        DataFrame: Resulting Dataframe
    """
    return pd.read_csv(
        filepath,
        memory_map=True,
        compression="gzip",
        sep=",",
        quotechar='"',
        error_bad_lines=False,
        parse_dates=[["Date", "TimeBarStart"], "ExpirationDate"],
        usecols=[
            "Date",
            "TimeBarStart",
            "CallPut",
            "Strike",
            "ExpirationDate",
            "CloseAskPrice",
            "CloseBidPrice",
            "UnderCloseBidPrice",
        ],
        dtype={
            "Date_TimeBarStart": object,
            "CallPut": object,
            "Strike": float,
            "ExpirationDate": object,
            "CloseBidPrice": float,
            "CloseAskPrice": float,
            "CloseAskSize": float,
            "UnderCloseBidPrice": float,
        },
    )


if __name__ == "__main__":
    main()