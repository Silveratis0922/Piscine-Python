import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file and returns its DataFrame.
    """
    try:
        if not path.endswith('.csv'):
            raise AssertionError("Need CSV file.")
        df = pd.read_csv(path)
        if df.empty:
            raise AssertionError("File is empty.")
        print("Loading dataset of dimensions", df.shape)
        return df.head()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
    except FileNotFoundError:
        print(f"{FileNotFoundError.__name__}: File does not exist.")
