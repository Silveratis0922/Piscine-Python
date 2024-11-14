import pandas as pd
# import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file and returns its DataFrame.
    """
    try:
        if not path.endswith('.csv'):
            raise AssertionError("Need CSV file.")
        df = pd.read_csv(path, index_col="country").T
        if df.empty:
            raise AssertionError("File is empty.")
        print("Loading dataset of dimensions", df.shape)
        return df
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
    except FileNotFoundError:
        print(f"{FileNotFoundError.__name__}: File does not exist.")


# def load(path: str) -> pd.DataFrame:
#     country = "Andorra"
#     df = pd.read_csv(path, index_col="country").T
#     print("Loading dataset of dimensions", df.shape)
#     plt.plot(df.index, df[country])
#     plt.title(f"{country} Life expectancy Projections")
#     plt.xlabel("Year")
#     plt.xticks(df.index[::40])
#     plt.ylabel("Life expectancy")
#     plt.show()
#     return df


# def load(path: str) -> pd.DataFrame: # Series Methode
#     country = "France"
#     df = pd.read_csv(path, index_col="country")
#     df = df.loc[country]
#     print(df)
#     print("Loading dataset of dimensions", df.shape)
#     plt.plot(df.index, df.values)
#     plt.title(f"{country} Life expenctancy Projections")
#     plt.xlabel("Year")
#     plt.xticks(df.index[::40])
#     plt.ylabel("Life expectancy")
#     plt.show()
#     return df

# def load(path: str) -> pd.DataFrame:
#     country = "France"
#     df = pd.read_csv(path)
#     df = df.loc[df["country"] == country]
#     print(df)
#     print("Loading dataset of dimensions", df.shape)
#     plt.plot(df.columns[1:], df.iloc[0, 1:].values)
#     plt.title(f"{country} Life expenctancy Projections")
#     plt.xlabel("Year")
#     plt.xticks(df.columns[1::40])
#     plt.ylabel("Life expectancy")
#     plt.show()
#     return df
